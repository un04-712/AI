"""
join方法:在进程中可以阻塞主进程的执行,直接等待子进程全部完成之后才继续运行主进程
后面的代码


"""
from multiprocessing import Process
import time

def func(name):
    print(f'{name}任务开始')
    time.sleep(5)
    print(f'{name}任务执行完毕')

if __name__=="__main __":

    p = Process(target=func, args=('写讲话稿',))

    p.start()
    p.join()
    print('主进程')

# def func(name):
#     print(f'{name}任务开始')
#     time.sleep(5)
#     print(f'{name}任务执行完毕')
#
# if __name__ == "__main__ ":
#     #得到进程操作对象
#     p1=Process(target=func,args=('写讲话稿1',))
#     p2=Process(target=func,args=('写讲话稿2',))
#     p3=Process(target=func,args=('写讲话稿3',))
#
# # 启动进程
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     print('主进程')