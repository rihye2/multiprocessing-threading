"""
I/O Bound(1) - synchronous
    - request

"""
import requests
import time

def request_site(url, session):
    # print(session)
    # print(session.headers)

    with session.get(url) as response:
        print(f'[Read Contents: {len(response.content)}, Status Code: {response.status_code}] \
              from {url}')


def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)



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
