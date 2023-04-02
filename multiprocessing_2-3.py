"""
Parallelism with Multiprocessing - Multiprocessing(3) - processPoolExecutor
Keyword - processPoolExecutor, as_completed, futures, timeout, dict 

~~PoolExecutor : 추상화 package, 코드를 직관적으로 사용하기 좋게 제공
future Object: 예약된 작업 
as_completed에 넣어서 실행을 해서 결과를 받아옴
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request 

#조회 url multiprocessing으로 방문
URLS = [
    'http://www.daum.net',
    'http://www.cnn.com/',
    'http://www.naver.com',
    'https://www.youtube.com/',
    'https://www.google.com/'
]

#실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
    
def main():
    #processpoll context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        #Future load (실행 x, 적재)
        future_to_url = {executor.submit(load_url, url, 50): url for url in URLS} #dict

        #실행
        for future in as_completed(future_to_url):
            #key값이 Future 객체
            #value 값이 url
            url = future_to_url[future]

            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r pasge is %d bytes' % (url, len(data)))

if __name__ == '__main__':
    main()