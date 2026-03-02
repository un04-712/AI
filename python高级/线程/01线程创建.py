"""
进程:资源单位
线程:执行单位

创建进程: 申请内存空间:消耗资源
拷贝代码:消耗资源
创建线程:  在一个进程可以创建多个线程,线程不需要再次申请内存空间,不需要拷贝代码

"""


from threading import Thread
import time



# 方式1
def task(name):
    print(f'{name}任务开始')
    time.sleep(3)
    print(f'{name}任务结束')

t = Thread(target=task,args=('悟空',))
t.start()


print('主线程')

# 方式2
class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'{self.name}任务开始')
        time.sleep(3)
        print(f'{self.name}任务结束')
t = MyThread('悟空')
t.start()
print('主线程')