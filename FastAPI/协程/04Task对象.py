"""
    Task对象 方便我们往事件里面添加任务
    asyncio.create_task(协程)  添加任务 将任务添加到事件循环 返回的是一个task对象
    task.cancel() 任务终止


"""
import asyncio


# async def nested():
#     print('进入IO')
#     await asyncio.sleep(1)
#     print('结束IO')
#     return 42
#
#
# async def main(name):
#     print(name,'start')
#     task = asyncio.create_task(nested()) #将任务添加到事件循环 返回的是一个task对象
#     res = await task #这里是task对象 task对象会等待任务完成将线程切换给其他任务
#     #但这里的nested()已经加入到事件循环，由事件循环调度
#     print(res)
#
# async def main2(name):
#     print(name,'start')
#     task = asyncio.create_task(nested()) #将任务添加到事件循环 返回的是一个task对象
#     task.cancel()
#     res = await task #由于task任务已经被移除 不可能等到返回结果 这里会一直等待 不会执行下面的程序
#     print('返回最后的结果',res)
#
#
# #这里会等待两个任务完成
# asyncio.run(asyncio.wait([main('任务1'),main2('任务2')]))

"""
    执行过程 ： 
                首先执行任务1,2中的一个，假设先执行任务2，提交nested任务到事件循环
    等待task任务执行完毕。
               再执行任务1，同样也会提交nested任务到事件循环，  等待task任务执行完毕。
               进入到任务2提交的nested对象中，输出进入IO，遇到延时阻塞，切换到任务1中的一个nested对象中，
    输出进入IO遇到延时阻塞 
                1s之后任务二中nested任务输出结束IO，返回42，接着任务一中nested任务输出结束IO，返回42。
                最后main('任务1')和main('任务2')会拿到各自返回结果并输出，主线程结束
"""

"""-------------------------------------在协程中创建多个任务对象(task列表)------------------------------------"""
# 兼容python3.7以上所有版本
async def nested():
    print('进入IO')
    await  asyncio.sleep(1)
    print('结束IO')
    return 42


async def main():
    # 方法1
    # task1 =  asyncio.create_task(nested())
    # task2 = asyncio.create_task(nested())
    # res1 =  await task1
    # res2 = await task2
    # print(res1,res2)
    # 方法2
    # done : 存放执行完成的任务
    # pending: 默认不填  当指定timeout参数时  存放未执行完成的任务
    done, pending = await asyncio.wait([asyncio.create_task(nested(), name='a'), asyncio.create_task(nested(), name='b')])
    print(done)

    for task in done:  # py3.8之后每个任务会有name属性,可以通过该属性区分不同任务
        print(task.get_name(), task.result())


# 执行main函数
asyncio.run(main())



