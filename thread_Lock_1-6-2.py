"""
1-6.py
동기화 코드 변경

"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading

class FakeDataBase:
    #공유 변수(value)
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
        #별도의 stack 영역
    
    #변수 update 함수
    def update(self, n):
        logging.info('Thread %s : staring update', n)
        #mutex & Lock이 필요한 지점 Thread synchronization 필요(동기화)

        #Lock획득 방법1
        # self._lock.acquire()
        # logging.info('Thread %s has lock', n)

        # local_copy = self.value
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy

        # logging.info('Thread %s about to release lock', n)

        # #Lock 반환
        # self._lock.release()



        #Lock 획득 방법 2
        with self._lock:
            logging.info('Thread %s has lock', n)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.info('Thread %s about to release lock', n)


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

00:13:57: Testing update. Starting value is 0
00:13:57: Thread First : staring update
00:13:57: Thread First has lock
00:13:57: Thread Second : staring update
00:13:57: Thread First about to release lock
00:13:57: Thread First: finishing update
00:13:57: Thread Third : staring update
00:13:57: Thread Second has lock
00:13:58: Thread Second about to release lock
00:13:58: Thread Second: finishing update
00:13:58: Thread Third has lock
00:13:58: Thread Third about to release lock
00:13:58: Thread Third: finishing update
00:13:58: Testing update. End value is 3


'''