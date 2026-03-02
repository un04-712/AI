"""
    信号量：在不同阶段，可能对应不同的技术点，对于并发编程，它指的是锁

    它可以用来控制同时访问特定的资源的线程数量，通常用于某些资源有明确访问数量限制的场景
    简单来说就是限流


"""
from threading import Semaphore, Thread
import time
import random

sq = Semaphore(5)
def task(name):
     sq.acquire()
     print(name,'抢到车位')
     time.sleep(random.randint(3,5))
     sq.release()

if __name__ == '__main__':
    for i in range(25):
        t = Thread(target=task,args=(f'宝马{i}',))
        t.start()
    