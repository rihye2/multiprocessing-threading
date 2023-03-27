import logging
import threading
import time

#thread 실행 함수
def thread_func(name):
    logging.info("Sub-Thread %s: start", name)
    time.sleep(3)
    logging.info("Sub-Thread %s: finish", name)


if __name__ == "__main__":
    #logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    #main thread
    x = threading.Thread(target=thread_func, args=("first",))
    logging.info("Main-Thread: before running thread")
    
    #sub-thread start
    x.start()
    
    #x.join()

    logging.info("main-Thread: wait for the thread to finish")
    logging.info("main-Thread: all done")


"""
00:15:26: Main-Thread: before creating thread
00:15:26: Main-Thread: before running thread
00:15:26: Sub-Thread first: start
00:15:26: main-Thread: wait for the thread to finish
00:15:26: main-Thread: all done
00:15:29: Sub-Thread first: finish

#부모 main thread가 끝나도 child thread는 실행 완료 후 끝남

---------------------------------------------------------------
#x.join을 추가할 경우 
child thread가 끝날때까지 main thread에서 대기

00:17:54: Main-Thread: before creating thread
00:17:54: Main-Thread: before running thread
00:17:54: Sub-Thread first: start
00:17:57: Sub-Thread first: finish
00:17:57: main-Thread: wait for the thread to finish
00:17:57: main-Thread: all done
"""