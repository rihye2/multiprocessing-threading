
"""
ThreadPoolExecutor 여러 스레드를 생성할 때, 편하게 할 수 있는 방법
keyword - Many Threads, concurrent.futures, ~~~PoolExecutor


그룹스레드
1. python 3.2 이상 표준 라이브러리
2. concurrent.futures
3. with 사용으로 스레드를 생성하거나, 소멸 라이프사이클 관리를 용이하게
4. 디버깅하기가 힘들다!
5. 대기중인 작업 -> 내부적으로 Queue에 담기고 -> 완료 상태를 조사 -> 결과 또는 예외 받아-> 단일화(캡슐화) 
"""


import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info('Sub-Thread %s: starting', name)
    result = 0
    for i in range(10000):
        result = result + i

    logging.info('Sub-Thread %s: finishing result: %d', name, result)

    return result

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    logging.info('Main-Thread: before creating and running thread')

    #실행방법1
    #max_workers: 작업의 개수가 넘어가면 직접 설정이 유리
    excutor = ThreadPoolExecutor(max_workers=3) #workers=3으로 설정했지만
    task1 = excutor.submit(task, ('First',))
    task2 = excutor.submit(task, ('second',)) #실제는2개

    #결과값 있을 경우
    print(task1.result())
    print(task1.result())


    #실행방법2
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task, ['First','Second', 'Third'])

        print(list(tasks))

if __name__ == '__main__':
    main()