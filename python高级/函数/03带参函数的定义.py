#位置参数：参数传递时实参的顺序和个数必须与形参保持一致
    #形参:函数在定义时括号里面申明的参数，用来在函数体内被执行相应的操作
    #实参:函数在调用时提供给函数的具体的数值或者变量
def sub(x,y):
    return x-y
print(sub(3,5))
print('*'*100)
#关键字参数：使用形参=实参的方式传递，不需要考虑形参的位置
#注意：位置参数必须在关键字参数之前传参
def sub(x,y,z):
    return z+x-y
print(sub(y=2,z=3,x=4))

print('*'*100)
#默认参数在定义时，直接对形参赋值，必须放在形参最右边

def setdate(day,month,year=2025):
    print(f'设置成功，日期为：{year}-{month}-{day}')
#默认参数在调用时，如果不需要修改默认参数的值，就可以不用传递，否则会将默认参数覆盖
setdate(16,1)
print('*'*100)
"""
        位置不定长参数:函数在定义时能够接收任意数量的位置参数
        定义时,用*args的形式表示 调用时传入的位置参数会被打包成一个元组
        注意:如果位置不定长参数右边还有其他参数，必须使用关键字传参才可以
"""


def myfunc1(*args):
    for i in args:
        print(i)
    print(type(args))
    print(len(args))
    print(args)
myfunc1(1,2,3,'asd')
myfunc1(1,2,3)
myfunc1(1, [1,2,3],3)

#得到传入参数的最大值 1,2,3,4,5
def max_args(*args):
    max_num = args[0]
    for i in args:
        if i > max_num:
            max_num = i
    return max_num
print(max_args(1,7,88,9,79))
print(max_args(1,7,79))

#如果右边有其他参数，必须使用关键字进行传参
def test1(*args,x,y):
    print(*args)
    print(x)
    print(y)
test1(1,2,3,4,x=2,y=3)

# 为什么要打包成元组而不是其他类型
#在元组有一个特性,打包,解包
# 打包 就是将多个值打包为一个元组

def test():
    return 1,2,3,4
ret = test()
print(ret)

# 解包:将一个元组的元素拆开分别赋值给对应的变量
def test(x,y,m,n):
    print(x,y,m,n)
args = (1,2,3,4)
test(*args)#位置参数解包
print('*'*100)
"""
    关键字不定长参数：**kwargs作为关键字不定长参数的标志，kwargs是程序员约定俗成的
    这个参数会将输入的关键字参数中的关键字当作键值对中的键，将关键字中的实参当作键值对的值

"""
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun(name='zmh',age=10)
fun(city='changsha')
fun(date='2005.3.15',sec='男',height=176)


# 对传入的参数的值进行相乘
def mul (**kwargs):
    result = 1
    for i in kwargs.values():
        result *= i
    return  result
print(mul(a=2,b=3))
print(mul(a=2,b=3,c=5,d=10))

# kwargs不能与其他参数同名
def test(x,*args, **kwargs):
    print(x)
    print(args)
    print(kwargs)
test(1,3,4,5,6,7,z=3,y=5)



