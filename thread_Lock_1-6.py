"""
Thread - Lock, DeadLock, Race Condition, Thread synchronization

1. Semaphore: 프로세스간 공유 된 자원에 접근 시 문제 발생 가능성이 있기 때문에
        한 개의 프로세스만 접근 처리 고안 -> 경쟁상태 예방
   
2. Mutex: 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것 -> 경쟁 상태 예방
3. Lock: 상호 배제를 위한 잠금처리 -> 데이터 경쟁
4. DeadLock: 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태)
5. Thread synchronization(스레드 동기화)를 통해 안정적으로 동작하게 처리(동기화 메소드, 동기화 블럭)
6. semaphore와 mutex의 차이
    모두 병렬 프로그래밍 환경에서 상호 배제를 위해 사용하지만, 
    뮤텍스틑 단일 스레드가 리소스 또는 중요 섹션을 소비하도록 허용하나
    세마포어는 리소스에 대한 제한된 수의 동시 access를 허용
    세마포어:  (열쇠가 3개있는 방문에 50명이 대기인원이 순서대로 문제가 생기지 않게 처리)
    뮤텍스: 1개의 방문에 여러 대기 인원이 기다리고 한번에 여러명이 들어가지 못함
    세마포어는 뮤텍스가 될 수 있으나 반대는 불가
"""


import logging
from concurrent.futures import ThreadPoolExecutor
import time


class FakeDataBase:
    #공유 변수(value)
    def __init__(self):
        self.value = 0
        #별도의 stack 영역
    
    #변수 update 함수
    def update(self, n):
        logging.info('Thread %s : staring update', n)
        #mutex & Lock이 필요한 지점 Thread synchronization 필요(동기화)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy

        logging.info('Thread %s: finishing update',n)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    #class instance화
    store = FakeDataBase()
    logging.info('Testing update. Starting value is %d', store.value)

    #with context 시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for n in ['First','Second','Third']:
            executor.submit(store.update, n)

    logging.info('Testing update. End value is %d', store.value)



'''

00:05:54: Testing update. Starting value is 0
00:05:54: Thread First : staring update
00:05:54: Thread Second : staring update
00:05:54: Thread First: finishing update
00:05:54: Thread Third : staring update
00:05:54: Thread Second: finishing update
00:05:54: Thread Third: finishing update
00:05:54: Testing update. End value is 2


'''