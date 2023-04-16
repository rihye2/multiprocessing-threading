"""
CPU Bound(1) - synchronous
    - CPU Bound: process의 I/O 최소화 하면서 대부분의 실행의 시간을 CPU만을 사용해서 작업

"""

import time

#실행함수1
def cpu_bound(number):
    return sum(i * i for i in range(number))

#실행함수2
def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    
    return result
def main():
    numbers=[3_000_000 + x for x in range(30)]
    

    start_time = time.time()


    total = find_sums(numbers)
    print(f'total list: {total}')
    print(f'Sum: {sum(total)}')

    duration = time.time() - start_time
    print(f'Duration: {duration} sec')


if __name__ == '__main__':
    main()

    """
    2.41512131690979 sec
    
    
    """