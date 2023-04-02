"""
Parallelism with Multiprocessing - Multiprocessing(2) - Naming,
Keyword - Naming, parallel processing 

"""
from multiprocessing import Process, current_process
import os
import time
import random

#실행
def square(n):
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name

    result = n*n
    print(f'Process ID: {process_id}, Process Name: {process_name}')

    print(f"Result of {n} square {result}")

#메인
if __name__ == '__main__':
    #부모 프로세스 id
    parent_process_id = os.getpid()
    print(f'parent process ID {parent_process_id}')

    processes = list()
    #프로세스 생성 및 실행
    for i in range(1, 10):
        #생성
        t = Process(name=str(i), target=square, args=(i,)) #name이라는 att로 지정 가능
        #배열에 담기
        processes.append(t)

        t.start()

    for process in processes:
        process.join()

    print('Main-processing Done')


"""

parent process ID 1410
Process ID: 1411, Process Name: 1
Result of 1 square 1
Process ID: 1412, Process Name: 2
Result of 2 square 4
Process ID: 1415, Process Name: 5
Result of 5 square 25
Process ID: 1416, Process Name: 6
Result of 6 square 36
Process ID: 1413, Process Name: 3
Result of 3 square 9
Process ID: 1414, Process Name: 4
Result of 4 square 16
Process ID: 1418, Process Name: 8
Result of 8 square 64
Process ID: 1419, Process Name: 9
Result of 9 square 81
Process ID: 1417, Process Name: 7
Result of 7 square 49
Main-processing Done


"""