"""
I/O Bound(2) - threading vs asyncIO vs multiprocessing
    - I/O Bound, asyncio

"""
#I/O Bound asyncio 예제
import aiohttp
import time
import multiprocessing
import asyncio
#threading보다 높은 코드 복잡도

async def request_site(session, url):
    
   async with session.get(url) as response:
       print('Read Contents {0}, from {1}'.format(response.content_length, url))



async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            #task 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
        # print(*tasks)
        # print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True) #작업이 완료되면 모아줌
        

def main():
    #test url
    urls=[
        "https://www.jython.org",
        # "https://olympus.realpython.org/dice",
        "https://realpython.com"
    ] * 5

    start_time = time.time()
    
    #async실행
    # asyncio.run(request_all_sites(urls))
    asyncio.get_event_loop().run_until_complete(request_all_sites(urls))
    duration = time.time() - start_time

    print(f"Downloaded {len(urls)} sites in {duration} seconds")

if __name__ == "__main__":
    main()
