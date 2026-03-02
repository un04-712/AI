"""
获取pid       current_process().pid   os. getpid()

杀死进程        p1.terminate()
进程是否存活      p1.is_alive()

"""

import time
from multiprocessing import Process, current_process


import os

def task(name='子进程'):
    print(f'任务{current_process().pid}执行中')
    print(f'{name}{os.getpid()}执行中')#获得自己的PID
    print(f'{name}的父进程{os.getppid()}执行中')# 获得父pid
    time.sleep(20)

if __name__ == "__main__":
    p1 = Process(target=task)
    p1.start()
    p1.terminate()      #杀死进程 cmd:taskkill pid
    print(p1.is_alive())         # 判断进程是否存活
    print('主进程',os.getpid())
    print('主进程的父进程',os.getppid())


