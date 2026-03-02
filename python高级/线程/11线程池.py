"""
    池：用来保证计算机硬件安全的情况下，最大限度利用计算机资源

    降低程序运行效率，但能保证数据安全

"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

# # 线程池的使用 不查看函数返回结果

# print(3 or 1)
# print(0 or 1)
# print(0 or -23)
# print(1 or 3)
# pool= ThreadPoolExecutor(10) #不传参,默认开设的线程数量是我们cpu核数+4
#
# def task(name):
#    print(name)
#    time.sleep(3)
#
# if __name__ == '__main__':
#    for i in range(50):
#        pool.submit(task,i)#往线程池中提交任务,异步提交 这里线程如果超过线程池数量需要排队

# 线程池的使用 查看函数返回结果

# print(3 or 1)
# print(0 or 1)
# print(0 or -23)
# print(1 or 3)
pool=ThreadPoolExecutor() #不传参,默认开设的线程数量是我们cpu核数+4

def task(name):
    print(name)
    time.sleep(3)
    return name+10

if __name__ == '__main__':
    f_list = []
    for i in range(50):
        future= pool.submit(task,i)#往线程池中提交任务,异步提交 这里线程如果超过线程池数量需要排队
        f_list.append(future)

    pool.shutdown()#关闭线程池,等待线程池中所有的任务运行完毕
    for future in f_list:
        print('函数返回结果',future.result())