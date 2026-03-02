"""
    GIL 全局解释锁：在cpython中，GIL是一把互斥锁，用来阻止用一个线程下的多个线程同时执行，
    也就是说在同一个进程下的多个线程，多个CPU不能并行，一次只有cpu来执行
    核心原理：在解释器里面加互斥锁
    加锁原因：如果多个运行，导致python的内存管理线程不是安全的
    总结：
        1、GIL不是python的特点，而是CPYTHON解释器独有的
        2、GIL会导致同一个进程下的多个线程不能同时执行，无法利用多核能力
        3、GIL的目的是保证解释器级别的数据安全
        4、写代码的时候，该怎么写就怎么写，不用考虑GIL

    问题：python多线程无法利用多核优势，即使有多个核，一次也只能使用一个

    分情况：
        单核：10个任务    (计算机密集型/IO密集型)
        多核：10个任务    (计算机密集型/IO密集型)

    多核：
        计算机密集型(大量的计算操作)每一个任务需要花费的时间是10s cpu有十个核
"""
#计算密集型任务
from threading import Thread
from multiprocessing import Process
import time
# def task():
#     res = 0
#     for i in range(10000000):
#         res+=i
#
# if __name__ == '__main__':
#     start = time.time()
#     task_hand = []
#     for i in range(8):
#         p = Process(target=task)      # 进程花费时间:1.9261643886566162
#         # p = Thread(target=task)         # 线程花费时间:3.1904659271240234
#         p.start()
#         task_hand.append(p)
#     for t in task_hand:
#         t.join()
#     end = time.time()
#     print('总耗时',end-start)




#计算I/O密集型任务

def in_task():
    with open("test.txt",'w') as f:
        for _ in range(100000):
            f.write("hello world\n")

    with open("test.txt", 'r') as f:
        for _ in range(100000):
            lines = f.readlines()

if __name__ == '__main__':
    start = time.time()
    task_handle = []
    for i in range(8):
        # p = Process(target=in_task)  # 进程花费时间： 5.161083459854126    1.994067907333374
        p = Thread(target=in_task)     # 线程花费时间：3.5235466957092285  2.886737108230591
        p.start()
        task_handle.append(p)
    # 等待所有任务执行完毕
    for i in task_handle:
        i.join()
    end = time.time()
    print("总耗时：",end-start)