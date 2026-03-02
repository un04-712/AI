
"""同步执行任务"""
import time


# def d():
#      for _ in range(3):
#          print('d')
#          time.sleep(2)
#
# def m():
#     for _ in range(3):
#         print('m')
#         time.sleep(2)
#
# start = time.time()
# d()
# m()
# end = time.time()
# print("花费时间:",end - start)  # 12.002875804901123


"""协程方式执行任务  主要了解协程的实现方式，以及在IO密集型下发挥的作用 """
from gevent import monkey  # 导入猴子补丁
monkey.patch_all()  # 打上猴子补丁   socket,select,time,threading,time等模块被替换为协程版本，非阻塞版本

from gevent import spawn  #  spawn 可以帮我们检测IO任务 实现单线程下遇到I/O状态就切换

def d():
     for _ in range(3):
         print('d')
         time.sleep(2)
def m():
    for _ in range(3):
        print('m')
        time.sleep(2)

start = time.time()
g1 =  spawn(d) # 添加需要检测IO任务的函数  返回协程对象
g2 = spawn(m)

# 等待协程执行完毕
g1.join()
g2.join()
end = time.time()
print("花费时间:",end - start)  # 6.043004989624023