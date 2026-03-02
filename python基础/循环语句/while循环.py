"""
    while循环：
        while 条件：
            代码块
        如果条件满足返回结果为True，则进入while循环去执行代码块，执行完毕后再次判断条件返回结果
        知道条件返回结果为False，退出循环
        2、嵌套的while格式
        while 条件1:
            while 条件2：
                代码块


"""

import random
#输出1-100以内的偶数
"""
num = 1
while num <= 100:
    num += 1
    if num %2 == 0:
        print(num)
"""

"""
    随机数模块:random
    random.randint(a,b)     返回a到b之间的一个随机整数
    random.random()     返回[0，1)之间的一个随机小数
    计算机生成的是伪随机数种子，所以通过设定成相同的随机数种子，可以每次生成相同的随机数
    random.seed()       生成随机数种子
    random.randrange    根据start stop step参数来确定随机数的取值
    random.uniform(a,b)      返回一个从a到b的一个随机数
random.seed(2)
print(random.random())

"""
#生成1-50之间的随机数，其中要包含小数
a = random.random()
print(random.randint(1,49) + a )
