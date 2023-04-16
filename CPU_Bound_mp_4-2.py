"""
CPU Bound(1) - multiprocessing
    - CPU Bound: process의 I/O 최소화 하면서 대부분의 실행의 시간을 CPU만을 사용해서 작업

"""

import time
from multiprocessing import current_process, Array, Value, Manager, Process, freeze_support
import os

#실행함수1
def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name

    #process 정보 출력
    print(f'process id: {process_id}, process name: {process_name}')

    total_list.append((sum(i * i for i in range(number))))

    return sum(i * i for i in range(number))

#실행함수2
def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    
    return result
def main():
    numbers=[3_000_000 + x for x in range(30)]
    

    #process list 선언
    processes = list()
    #process 공유 manager
    manager = Manager()
    #process 공유 (list 획득)
    total_list = manager.list()

    start_time = time.time()
    #process 생성 및 실행
    for i in numbers:
        #생성
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list,))
        processes.append(t)
        t.start()

    #join
    for process in processes:
        process.join()

    print()


    
    print(f'total list: {total_list}')
    print(f'Sum: {sum(total_list)}')

    duration = time.time() - start_time
    print(f'Duration: {duration} sec')


if __name__ == '__main__':
    main()

    """
    Duration: 0.7267415523529053 sec
    """