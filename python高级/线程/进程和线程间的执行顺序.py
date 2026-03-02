import time
from multiprocessing import Process
from threading import Thread

from multiprocessing import Process
import os

def get_info(a):
    time.sleep(3)
    print("get_info", a)

    # 获取pid
    # print("get_info",os.getpid())


if __name__ == '__main__':
    # 创建10个子进程
    for i in range(100):
        sub_process =  Process(target=get_info,args=(i,))
        sub_process.start()




#
# def task(a):
#     time.sleep(1)
#     print("get0_info",a)
#
# if __name__ == '__main__':
#     for i in range(5):
#         T1 = Thread(target=task,args=(i,))
#         T1.start()