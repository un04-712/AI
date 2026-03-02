"""
       死锁
"""

import time
from threading import Thread, Lock, current_thread

mutex1 = Lock()
mutex2 = Lock()

#死锁现象(了解)
def task():
    mutex1.acquire()
    print(f'{current_thread().name}抢到锁1')
    mutex2.acquire()
    print(f'{current_thread().name}抢到锁2')
    mutex2.release()
    mutex1.release()

    mutex2.acquire()
    print(f'{current_thread().name}抢到锁2')
    time.sleep(1)
    mutex1.acquire()
    print(f'{current_thread().name}抢到锁1')
    mutex2.release()
    mutex1.release()

if __name__ =='__main__':
    for i in range(8):
        t = Thread(target=task)
        t.start()