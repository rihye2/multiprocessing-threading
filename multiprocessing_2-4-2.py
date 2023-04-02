"""
Parallelism with Multiprocessing - Multiprocessing(4) - Sharing state
Keyword - memory sharing, array, value 

"""

from multiprocessing import Process, current_process, Value, Array
import os

#process memory 공유 예제 (공유 패턴)

#실행함수
def generate_update_num(v: int):
    for _ in range(50):
        v.value += 1
    print(current_process().name, "data", v)

def main():
    parent_process_id = os.getpid()

    print(f'Parent process ID {parent_process_id}')

    processes = list()

    #process memory 공유 확인
    
    """변경"""
    #from multiprocess import shared_memory 사용가능(데이터 공유시 사용, 3.8부터)
    #from multiprocess import Manager 사용가능
    #Value(typecode or tpye)
    # share_numbers = Array('i', range(50))
    share_value = Value('i', 0) #int

    for _ in range(1, 10):
        #생성
        p = Process(target=generate_update_num, args=(share_value,))

        #배열에 담기
        processes.append(p)

        p.start()

    for p in processes:
        p.join()
    
    print('Final Data in parent process', share_value.value)
if __name__ == '__main__':
    main()

"""

Parent process ID 1796
Process-1 data 50
Process-2 data 50
Process-4 data 50
Process-3 data 50
Process-5 data 50
Process-6 data 50
Process-7 data 50
Process-8 data 50
Process-9 data 50
Final Data in parent process 0

"""