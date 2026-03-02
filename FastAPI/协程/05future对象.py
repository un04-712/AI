"""
    Future(Task任务的基类) 是一个表示异步操作结果的占位符 ,属于低级别的对象

    用于在异步任务完成后存储和传递结果

"""
import asyncio

# 定义一个异步函数，接受一个Future对象作为参数
# async def f1(future):
#     print("f1 start")
#     await asyncio.sleep(3)
#     future.set_result('hello') # 设置Future对象的结果为hello
#
# async def main():
#     # 创建一个Future对象
#     future = asyncio.Future()
#     # 创建一个异步任务，并传入Future对象
#     asyncio.create_task(f1(future))
#
#     res = await  future
#     print(res)
#
# asyncio.run(main())


"""
     自定义函数中有可能发生阻塞 ，我需要通过await切换任务 但没有异步函数 ，应该怎么做 ？

"""
import time


# 同步函数
def f1(x):
    print(x)
    time.sleep(5)
    return 'hellof1'


# 异步函数
async def f2(x):
    print(x)
    # time.sleep(5)
    await asyncio.sleep(5)
    return 'hellof2'


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()
    # 对同步任务通过线程池去执行
    future_f1 = loop.run_in_executor(None, f1, 'hello f1')
    # 对异步任务通过事件循环(协程)去执行
    task_f2 = asyncio.create_task(f2('hello f2'))

    # 等待f1 和 f2的结果
    result1 = await future_f1
    result2 = await task_f2

    print(result1, result2)


asyncio.run(main())