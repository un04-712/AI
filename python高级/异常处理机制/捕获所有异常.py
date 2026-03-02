"""
    格式：
        try:
            #有可能发生异常的代码
        except Exception：
            #异常发生后要执行的代码
        else:
            #如果没有异常发生，在try执行完毕后会执行这里的代码
        finally：
            #不管有没有捕获到异常，最后都会执行这里的代码

"""
from logging import exception

#try:
#    exec1 = eval(input())
#except Exception as e :  #作用是将捕获到的异常对象赋值给变量e,这样可以使用e来引用和处理异常
#    print(e)
#else :
#    print('程序正常运行')
"""
    异常传递性：当一个函数或方法抛出一个异常，这个异常会被传递到调用方这里，如果调用者没有捕获到异常，那么程序会终止
"""
def method1():
    print('in method1')
    method2()
    print('out method1')

def method2():
    print('in method2')
    print(1/0)
    print('out method2')
try:
    method1()
except Exception as e:
    print(e)