from threading import Thread
import time
import os
age = 18
def task(name):
    global age
    age = 10
    print('子线程',os.getpid())
if __name__ == "__main__":
    t = Thread(target=task,args=('悟空',))
    t.start()
    t.join()
    print(age)
    print('主线程',os.getpid())

from threading import Thread, active_count, current_thread

def task():

    print(f'{current_thread().name}')
    time.sleep(1)

if __name__ == '__main__':
    t1 = Thread(target=task)
    t2 = Thread(target=task)
    t1.start()
    t2.start()
    print('活跃的线程数量',active_count())
    print('Ìm',current_thread().name)