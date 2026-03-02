"""
    池：用来保证计算机硬件安全的情况下，最大限度利用计算机资源

    降低程序运行效率，但能保证数据安全

"""

from concurrent.futures import ProcessPoolExecutor
import time
import os

pool= ProcessPoolExecutor()#不传参,默认开设的进程数量是cpu的核数

def task(name):
    print(name, os.getpid())
    time.sleep(3)
    return name+10

def call_back(res): 
    print('call back',res.result())

if  __name__ == '__main__':
    f_list = []
    for i in range (50):
        pool. submit(task,i).add_done_callback(call_back)

