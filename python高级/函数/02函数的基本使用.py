"""
    函数：
        def 函数名(参数(无参数可不填)):
            代码块
            return 参数值
    作用：为了代码的重复使用
    使用return结束函数，选择性的返回一个值给到调用方
    没有return默认返回None
    return按实际需求，可写可不写

    函数的基本组成;
            名称
            功能
            参数
            返回值

"""
#连续输出五句话
#函数不会主动执行，需要调用
def myfunc():
    """
    这是一个测试函数，会打印5句hello，world
    """
    for i in range(5):
        print('hello,world')
#函数的调用：函数名+()
myfunc()

help(myfunc)

#pass:在函数刚开始定义且没有功能是，作为一个占位符，防止编译器报错
def login():
    pass

def register():
    pass

def max_list(*args):
    max_num = args[-1]
    for i in args:
        if i > max_num:
            max_num = i
    return max_num
print(max_list(1,2,3,4,5,6,7,8,9))