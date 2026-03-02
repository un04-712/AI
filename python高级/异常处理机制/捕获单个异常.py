"""
    格式：
        try:
            #有可能发生异常的代码
        except 某个异常：
            #异常发生后要执行的代码
        else:
            #如果没有异常发生，在try执行完毕后会执行这里的代码
        finally：
            #不管有没有捕获到异常，最后都会执行这里的代码

"""

try:
    a = 1
    print(a)
except NameError:
    print('捕获到了异常')
else:
    print('没有捕获到异常')
finally:
    print('我最后执行')




try:
    num1 = eval(input())
    num2 = eval(input())
    print(num1/num2)
except ZeroDivisionError:
    print('除数不能为0')
else:
    print('代码运行正常,没有触发异常')
finally:
    print('不管有没有异常,我都会执行')