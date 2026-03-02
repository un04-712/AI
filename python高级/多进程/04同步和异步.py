"""
        同步:任务提交之后,原地等待任务的返回结果,等待的过程中不能做任何事情
        异步:任务提交之后,不在原地等待任务的返回结果,而是直接去处理其他事情
"""
import time
# 同步调用
def func() :
    print('任务开始')
    time.sleep(5)
    print('任务结束')
func()
print('hello')