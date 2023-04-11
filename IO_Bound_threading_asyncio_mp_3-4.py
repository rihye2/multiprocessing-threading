"""
I/O Bound(2) - threading vs asyncIO vs multiprocessing
    - I/O Bound, request, threading


    독립적, 병렬적 처리되는 작업 ->multiprocessing으로
    일반적 I/O Bound -> threading, asyncIO
"""
#I/O Bound multiprocessing Pool예제
import requests
import time
import multiprocessing

#각 프로세스 메모리 영역에 생성되는 객체 (독립적)
#함수 실행할 때 마다 객체 생성은 좋지 않다 (process에서)
#미리 생성해놓고 할당

session = None
def set_global_session():
    global session
    if not session:
        session = requests.Session()

def request_site(url):
    
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f'[{name} -> read contents: {len(response.content)}, Status Code: {response.status_code} from {url}]')



def request_all_sites(urls):
  
    #multiprocessing 실행
    #processes 갯수 조절 후 session 객체 및 실행 시간 확인
    
    #pool이 좋은점은 initializer될 때, 함수를 실행하고 pool을 생성
    #따라서 processes 4개가 set_global_session을 실행하고 session을 미리 생성
    #속도가 빨라짐!
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)


def main():
    #test url
    urls=[
        "https://www.jython.org",
        # "https://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 3

    start_time = time.time()
    
    request_all_sites(urls)
    
    duration = time.time() - start_time

    print(f"Downloaded {len(urls)} sites in {duration} seconds")

if __name__ == "__main__":
    main()
