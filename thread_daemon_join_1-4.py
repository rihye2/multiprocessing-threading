import logging
import threading
import time
"""
DaemonThread
- 백그라운드에서 실행(스레드 안에서 새롭게 스레드를 만들어 실행)
- 메인 스레드 종료시 즉시 종료
- 주로 background 무한 대기 이벤트 발생 실행하는 부분 담당
- 일반 스레드는 작업 종료시 까지 실행
"""

#thread 실행 함수
def thread_func(name, b):
    logging.info("Sub-Thread %s: start", name)
    
    for i in b:
        print(i)
    logging.info("Sub-Thread %s: finish", name)


if __name__ == "__main__":
    #logging format
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    #main thread
    x = threading.Thread(target=thread_func, args=("first",range(200)), daemon=True)
    y = threading.Thread(target=thread_func, args=("second",range(100)), daemon=True)
    logging.info("Main-Thread: before running thread")
    
    #sub-thread start
    x.start()
    y.start()

    #x가 daemonthread인가를 확인(일반스레드가 종료되면 종료되는 스레드인가?)
    print(x.isDaemon())

    #x.join()
    #y.join()
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