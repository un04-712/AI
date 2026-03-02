"""
    主线程运行完毕之后，不会立刻结束，要等待所有的子线程执行完毕才会结束
    因为主线程结束，就意味着主线程所在的进程结束了
"""
from threading import Thread,active_count
import time

def task(name):
    print(f'{name}还活着')
    time.sleep(3)
    print('活跃的线程数量',active_count())

    print(f'{name}正常死亡')
if __name__== '__main__':
    t1 = Thread(target=task,args=('妲己',))
    t1.daemon = False
    t1.start()
    time.sleep(1)
    print("纣王驾崩了")