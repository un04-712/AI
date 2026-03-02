#   局部变量：定义在函数内部的变量和参数

def fun():
    x = 1
    print(x)
#只在函数生效时存在，当函数执行完毕，便无法访问该变量

"""
    #全局变量：定义在函数外面的变量或者在函数内部使用global关键字修饰的变量
    注意：
        在函数内部可以访问到局部变量，但是函数外部无法访问局部变量
        函数内部局部变量和全局变量名字相同时，局部变量会覆盖掉全局变量
        global非必要时不用使用，应为global修饰的变量能在函数内部去修改全局
        变量的值
        
"""
y = 1
def fun1():
    x = 1
    print('函数修改之前的：',id(x))
    global y
    y = 10
    print('函数修改之后的：',id(y))

fun1()

# 关于列表的len函数实现
def len_list(my_list):
    count = 0
    for i in my_list:
     count += 1
    return count
print(len_list([1,4,3,6,'fsdDds',334.3, [123]]))

# AM#M 内置常量 (BIC built in constant ) WMm# 内置函数(BIF  built in Function )

# 函数名字或者变量名字和BIF名字相同,会导致调用不到BIF

def sum(my_list):
    result = 0
    for i in my_list:
        result += i
    return result
print(sum([1,2,3,4,5,6]))

