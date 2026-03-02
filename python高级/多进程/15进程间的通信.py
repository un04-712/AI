"""
    进程间的通信(IPC):管道 共享内存 信号 队列

"""

from multiprocessing import Process, Queue
def task1(q):
    q.put('宫保鸡丁')

def task2(g):
    print(q.get())

if __name__ == "__main__":
    q = Queue ()
    # 主进程与子进程进行通信
    p1 = Process(target=task1,args=(q,))
    p2 = Process(target=task2, args=(q,))
    p1.start()
    p2.start()
# print('主进程',q.get())# 主进程和子进程的通信


