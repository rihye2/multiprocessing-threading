"""
Parallelism with Multiprocessing - Multiprocessing(5) - Queue, Pipe
Keyword - Queue, Pipe, Communications between processes

"""

#process 통신구현 queue
from multiprocessing import Process, Queue, current_process
import time
import os


def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    #누적
    sub_total = 0

    for i in range(baseNum):
        sub_total += 1

    #produce
    q.put(sub_total)

    print(f'Process ID {process_id}, process Name: {process_name} ID: {id}')
    print(f'Result: {sub_total}')


def main():
    #parent process id
    parent_process_id = os.getpid()
    #출력
    print(f'Parent process Id {parent_process_id}')

    #process list 선언
    processes = list()

    start_time = time.time()
    #queue 선언
    q = Queue()

    for i in range(5):
        t = Process(name=str(i), target=worker, args=(i, 1000000, q))

        #배열에 담기
        processes.append(t)

        t.start()
    #Join
    for process in processes:
        process.join() #완료될떄까지 기다림

    print("------ %s seconds --------" % (time.time() - start_time))

    #종료 flag

    q.put('exit')

    total = 0
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp
    
    print('')

    print('Main-processing Total count = {}'.format(total))
    print('Main-Processing Done')


if __name__ == '__main__':
    main()


"""

Parent process Id 2149
Process ID 2153, process Name: 3 ID: 3
Result: 1000000
Process ID 2151, process Name: 1 ID: 1
Result: 1000000
Process ID 2150, process Name: 0 ID: 0
Process ID 2154, process Name: 4 ID: 4
Result: 1000000
Result: 1000000
Process ID 2152, process Name: 2 ID: 2
Result: 1000000
------ 0.036228179931640625 seconds --------

Main-processing Total count = 5000000
Main-Processing Done

"""