"""
I/O Bound(2) - asyncIO basic
    - asyncio


동시 프로그래밍 패러다임 변화
    - 싱글코어: 처리향상 미미, 저하 -> 비동기 프로그래밍이 대두(CPU연산, DB연동, API호출은 대기 시간이 늘어남(Block))
    asyncIO Nonblocking 비동기식

"""
import time
import asyncio
#비동기 함수에서 비동기함수를 호출할때 반드시 함수이름 앞에 await

async def exe_calculate_async(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calcuating...')
        await asyncio.sleep(1)
    print(f'{name} - {n} working done!')

async def process_async():
    start = time.time()

    await asyncio.wait([
        exe_calculate_async('One', 3),
        exe_calculate_async('two', 2),
        exe_calculate_async('three', 1)
    ])
    

    end = time.time()
    print(f'>>> total seconds: {end - start}')




def exe_calculate_sync(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calcuating...')
        time.sleep(1)
    print(f'{name} - {n} working done!')


def process_sync():
    start = time.time()

    exe_calculate_sync('One', 3)
    exe_calculate_sync('two', 2)
    exe_calculate_sync('three', 1)

    end = time.time()
    print(f'>>> total seconds: {end - start}')
if __name__ == '__main__':
    #sync 실행
    # process_sync()

    #async실행
    asyncio.run(process_async())
    #3.7이하
    # asyncio.get_event_loop().run_until_complete(process_async())


"""
process_sync()
One -> 1 of 3 is calcuating...
One -> 2 of 3 is calcuating...
One -> 3 of 3 is calcuating...
One - 3 working done!
two -> 1 of 2 is calcuating...
two -> 2 of 2 is calcuating...
two - 2 working done!
three -> 1 of 1 is calcuating...
three - 1 working done!
>>> total seconds: 6.007301568984985

process_async()
two -> 1 of 2 is calcuating...
One -> 1 of 3 is calcuating...
three -> 1 of 1 is calcuating...
two -> 2 of 2 is calcuating...
One -> 2 of 3 is calcuating...
three - 1 working done!
two - 2 working done!
One -> 3 of 3 is calcuating...
One - 3 working done!
>>> total seconds: 3.003926992416382

"""