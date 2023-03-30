"""
Prod vs Cons using Queue


keyword - 생산자 소비자 패턴(Producer/consumer pattern)

Producer/consumer pattern
 1. 멀티스레드 디자인 패턴의 정석
 2. 서버 프로그래밍의 핵심

 python Event 객체
 1. Flag 초기값(0)
 2. Set() 호출 ->1로 , Clear() -> 0, Wait(1: return, 0: 대기), isSet() -> 현flag 상태


"""

import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queue, event):
    """
    네트워크 대기 상태로 가정(서버)
    데이터 리딩, I/O작업..
    """
    while not event.is_set(): #flag = 0
        msg = random.randint(1, 11)
        logging.info('Producer got msg: %s', msg)
        queue.put(msg)
    logging.info('producer send event End')

def consumer(queue, event):
    """
    응답 받고 소비하는 것으로 가정 or DB저장
    
    """
    while not event.is_set() or queue.empty():
        msg = queue.get()
        logging.info(
            'cons storing msg: %s (size=%d)', msg, queue.qsize()
        )
    logging.info('consumer received event end')


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")


    pipeline = queue.Queue(maxsize=10)
    #queue의 size는 중요함
    """
    서비스하려는 환경에 맞춰 size를 정해야, 무한대로 담기면 
    서비스 하는 환경에서 처리를 그때 그때 하지 못하면, 병목이 일어날 수 있음
    
    """

    #event flag 초기값 0
    event = threading.Event()
    
    #with context시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        #실행 시간 조정
        time.sleep(2)
        logging.info("Main: about to set event")
        #이벤트 종료
        event.set()