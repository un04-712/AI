"""
    守护进程:与主进程同生共死


"""

from multiprocessing import  Process
import time

def task(name):
    print(name,'还活着')
    time.sleep(5)
    print(name,'正常死亡')
if __name__ == '__main__':
    p = Process(target=task,args=('苏妲己',))
    #方法一：守护进程，退出后子进程直接销毁，不在执行子进程代码
    # p.daemon =True
    #启动进程
    p.start()
    time.sleep(1)

    #方法二：让子进程直接销毁，终止执行，主进程退出之前，把所有子进程直接销毁
    p.terminate()
    print('纣王驾崩')