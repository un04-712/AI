"""
    递归锁:内部有一个计数器,每acquire一次计数器就会加1，每release一次就会减一

    只要计数器不为0，其他人就不能抢到这把锁
"""


import time
from threading import Thread, RLock, current_thread

mutex1 = RLock()
mutex2 = mutex1



#递归锁现象(了解)
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