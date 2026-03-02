"""
    异常是一种事件，在我们程序执行过程中产生，影响程序的正常执行

    一般情况下，python遇见错误的代码或者无法正常处理的程序就回产生异常并抛出，异常抛出后，可以被捕捉。捕捉后程序会按照某种机制继续运行
    如果对抛出的异常不做任何处理，那么程序会终止运行

"""
#KeyboardInterrupt  用户主动结束程序
# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)


#Attributeerror 尝试访问对象所没有的属性
#my_str = 'add'
#print(my_str.abc())

#typeError  操作非法类型
# a = 'desfj'
# b = 3
# result =a+b
# print(result)

#indexError 访问不存在的索引时触发
# my_list = [1,2,3]
# print(my_list(10))

#keyError   映射中没有键
# my_dict = {'name':'Alice','age':25}
# value = my_dict["address"]