"""
队列:先进先出
栈:后进先出

Queue.put
Queue.put_nowait()
Queue.get
Queue.get_nowait()
· Queue. full
Queue.empty
"""
import queue
from multiprocessing import Process, Queue

q = Queue(6)

q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')
q.put('f')


#

# q.put('g')#数据满,一直等待,直到队列能存入下一个数据
#

# q.put('g', timeout=3) # 队列满, 当超时时间到达之后直接报错

# q.put_nowait('g') # 队列满不等待直接报错

# v1 = q.get()
# print(v1)
# v1 = q.get()
# print(v1)
# v1 = q.get()
# print(v1)
# v1 = q.get()
# print(v1)
# v1 = q.get()
# print(v1)
# v1 = q.get()
# print(v1)

#v1=q.get()#数据空,一直等待,直到有数据入列
# v1=q.get(timeout=3)# 3s内没有数据直接报错

# q.get_nowait() # 队列满不等待直接报错
#
# print(v1)

"""
        后进先出队列
"""
#
# q = queue.LifoQueue()
# q.put('3')
# q.put(4)
# q.put([1])
# q.put((12,))
# q.put(13)
#
# print(q.get())
