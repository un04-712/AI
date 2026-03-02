"""
    生产者:
    消费者:
    媒介:

"""

import random
import time
from multiprocessing import Process, Queue, JoinableQueue
def producer(name, food, q):
    for i in range(8):
        time.sleep(random.randint(1, 3))
        print(f'{name}7{food}{i}')
    q.put(f'{food}{i}')
def consumer(name, q):
    while True:
        food = q.get()
        if food == '鹤顶红':
            break
        time.sleep(random.randint(1, 3))
        print(f'{name}"2] {food}')
        q.task_done()  # 告诉队列,已经拿走了一个数据,并且已经处理完了

if __name__ == '__main __ ':
    # q = Queue ()

    q = JoinableQueue ()
    p1 = Process(target=producer,args=('中华小当家','黄金炒饭',q))
    p2 = Process(target=producer,args=('神厨小福贵’,‘佛跳墙',q))

    c1 = Process(target=consumer, args=('i/V&', q))
    c2=Process(target=consumer,args=('悟空',q))

    p1.start()
    p2.start()

    c1.daemon = True
    c2.daemon = True

    c1.start()
    c2.start()

    p1.join()
    p2.join()

    q.join() # 等待队列中所有的数据被取完

    # q.put('鹤顶红')
    # q.put('鹤顶红')

    print('主进程')