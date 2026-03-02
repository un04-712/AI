"""
        嵌套函数：如果在一个函数内部定义了一个函数，这个函数就叫嵌套函数，外部外面叫外函数，内部叫内函数
        2、内部函数只能在外部函数调用，其他情况时无法访问的
        嵌套函数的特性：内函数访问外函数某个变量时修改变量不会随外函数的调用完毕而销毁，而是被内函数所保留
"""
#闭包函数:如果内部函数使用外函数的局部变量，并且外函数把内函数返回出来的过程叫闭包，里面的函数叫闭包函数

def multiplier(factor):
    def multiply_by (x):
        return x * factor
    return multiply_by  #    注意这里返回的就是函数 可以供外部调用

# 创建一个乘以2的函数
times_2 = multiplier(2)
print(times_2(5))



# global和 nonlocal不能对同一变量生效
x = 3
y = 3
def outer_func():
    x = 1
    def inner_func():
        global y    #通过global关键字可以修改全局变量的值
        nonlocal x  #通过nonlocal关键字可以修改外函数变量的值
        x = 2
        y = 2
        print(y)
        print('内函数x:',x)
    inner_func()
    print('外函数x:',x)
    return
outer_func()
print(x)
print(y)



x = 3
def outer_func():
    global x
    x = 1
    def inner_func():
        # nonlocal x
        x = 2
        y = 2
        print(x,y)
        return x

    x = inner_func()
    print(x)

outer_func()
print(x) # 2











