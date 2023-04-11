"""
I/O Bound(2) - threading vs asyncIO vs multiprocessing
    - I/O Bound, request, threading

"""
#I/O Bound Treading 예제
import requests
import time
import concurrent.futures 
import threading

import multiprocessing
#각 스레드에 생성되는 객체
#각 스레드마다 별도의 독립적인 변수 메모리영역을 할당받아서 사용
#독립된 네임스페이스 영역을 사용한다.
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local = requests.Session()
    return thread_local.session()

def request_site(url):
    #3-2
    # print(session)
    # print(session.headers)

    # with session.get(url) as response:
    #     print(f'[Read Contents: {len(response.content)}, Status Code: {response.status_code}] \
    #           from {url}')
    

    #session 획득
    session = get_session()
    with session.get(url) as response:
        print(f'[read contents: {len(response.content)}, Status Code: {response.status_code} from {url}]')



def request_all_sites(urls):
    # with requests.Session() as session:
    #     for url in urls:
    #         request_site(url, session)
    
    #3-2
    #multi-threading 실행
    #반드시 max_worker 갯수 조정 후 session 객체 확인
    # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # executor.map(request_site, urls)

    #multiprocessing 실행
    #processes 갯수 조절 후 session 객체 및 실행 시간 확인
    
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
