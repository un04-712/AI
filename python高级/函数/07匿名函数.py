"""
        匿名函数：一把运用于在干函数体中只有一句且只有一个返回值的时候使用
        格式：
            lambda  参数列表：表达式
            参数列表：和函数参数列表一样
            表达式：函数体
            特性：
                lambda函数是匿名的，自带return
                lambda函数可以使用任意数量的参数，但只能包含一个表达式
                lambda函数只返回一个值，这个值就是表达式的结果
                lambda函数生命周期很短，调用后立即回收
"""
def add(x,y):
    return x+y
print(add(3,4))


ls = lambda x,y:x*y
print(ls(2,4))

ls = lambda x,y=3:x*y
print(ls(x=3))



#判断一个数是不是偶数

func = lambda x: x%2 == 0
num =int(input('请输入要判断的数:'))
print(func(num))

# 使用lambda表达式配合map函数完成对列表中的所有元素加10
ls = [x for x in range(10)]

result = list(map (lambda x:x+10, ls) )
print(result)

# 匿名函数的参数也可以使用默认参数
add = lambda x, y = 1: x + y
print(add(y=1,x=3))

func = lambda *args : args

print(func( [1,2,3,4],2,43,4))

