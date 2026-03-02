"""
    格式：
        try:
            #有可能发生异常的代码
        except (第一个异常，第二个异常)：
            #异常发生后要执行的代码
        else:
            #如果没有异常发生，在try执行完毕后会执行这里的代码
        finally：
            #不管有没有捕获到异常，最后都会执行这里的代码

"""
# 连续捕获 SyntaxError NameError
#方法1
try:
     exec1 = eval(input())
except SyntaxError:
    print('语法有问题')
except NameError:
    print('没有这个变量')
else :
    print('程序正常运行')

print('*'*100)
#方法2
try:
    exec1 = eval(input())
except (SyntaxError, NameError) :
    print('捕获到异常')
else :
    print('程序正常运行')