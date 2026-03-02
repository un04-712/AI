"""
创建进程:
    os.fork() linux环境
    multiprocessing 主要
    subprocess      运维使用，功能不多

    Process()参数
        target:执行任务目标，这里指函数名
        name:进程名    一般不用设置
        group:进程组   目前只能使用None
        args:以元组的形式给执行任务传参
        kwargs:以字典的形式给执行任务传参
"""
#方法一

from multiprocessing import Process
import time

def func(name):
    print(f'{name}任务开始')
    time.sleep(5)
    print(f'{name}任务执行完毕')

if __name__=="__main__":

    p = Process(target=func,args=('讲话稿',))

    #启动进程
    p.start()
    print('主进程')




# 方法二
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.task_name = name
    def run(self):
        print(f'{self.task_name}任务开始')
        time.sleep(2)
        print(f'{self.task_name}任务执行完毕')

if __name__ == '__main__':
    p = MyProcess('测试')
    p.start()
    print('主进程')

# from multiprocessing import Process
# import time
#
# class my_process(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         print(f"{self.name}程序开始执行")
#         time.time(2)
#         print(f"{self.name}进程执行完毕")
#
# if "__name__" == "__main__":
#     p = my_process("测试")
#     p.start()
#     print('主进程')