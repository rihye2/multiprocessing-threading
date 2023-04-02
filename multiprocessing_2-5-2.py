"""
Parallelism with Multiprocessing - Multiprocessing(5) - Queue, Pipe
Keyword - Queue, Pipe, Communications between processes

"""

#process 통신구현 Pipe
from multiprocessing import Process, Pipe, current_process
import time
import os


def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name

    #누적
    sub_total = 0

    for i in range(baseNum):
        sub_total += 1

    #produce
    conn.send(sub_total)
    conn.close() #Pipe는 반드시 close
    print(f'Process ID {process_id}, process Name: {process_name} ID: {id}')
    print(f'Result: {sub_total}')


def main():
    #parent process id
    parent_process_id = os.getpid()
    #출력
    print(f'Parent process Id {parent_process_id}')

 
    start_time = time.time()
    #pipe는 부모와 자식의 1:1 통신

    parent_conn, child_conn = Pipe()

    t = Process(name=str(1), target=worker, args=(1, 5000000, child_conn))

    t.start()
    #Join
    
    t.join() #완료될떄까지 기다림

    print("------ %s seconds --------" % (time.time() - start_time))

    
    print('')

    print('Main-processing Total count = {}'.format(parent_conn.recv()))
    print('Main-Processing Done')


if __name__ == '__main__':
    main()


"""

Parent process Id 2303
Process ID 2304, process Name: 1 ID: 1
Result: 5000000
------ 0.09908246994018555 seconds --------

Main-processing Total count = 5000000
Main-Processing Done

"""