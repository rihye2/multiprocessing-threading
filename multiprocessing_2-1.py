"""
Parallelism with Multiprocessing - Multiprocessing(1) - Join, is_alive
Keyword - Multiprocessing, processing state

하나의 프로세스 생성 후 단일로 실행 예제
"""
from multiprocessing import Process
import time 
import logging

def proc_func(name):
    print('Sub-Process {}: start'.format(name))
    time.sleep(3)
    print('Sub-Process {}: finish'.format(name))

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    p = Process(target=proc_func, args=('First', ))

    logging.info('Main-Process: before creating Process')

    p.start()
    logging.info('Main-Process: During process')


    #즉시 종료
    # logging.info('Main-process: Terminated process')
    # p.terminate()

    logging.info('Main-Process: join process')
    p.join()


    #process 상태확인
    print(f'process p is alive: {p.is_alive()}')
if __name__ == '__main__':
    main()


"""
21:06:10: Main-Process: before creating Process
21:06:10: Main-Process: During process
21:06:10: Main-Process: join process
Sub-Process First: start
Sub-Process First: finish
process p is alive: False



"""