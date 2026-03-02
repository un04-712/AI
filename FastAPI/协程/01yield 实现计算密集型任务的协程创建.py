"""协程实现多个任务  在单线程下是实现并发 单线程下实现多个任务的切换"""
import time



def f1():
    n = 0
    for i in range(500000000):
        n+=1
        yield

g = f1()

def f2():
    n = 0
    for i in range(500000000):
        n+=1
        next(g)

start = time.time()
f2()
end = time.time()
print("总耗时长为:",end-start)