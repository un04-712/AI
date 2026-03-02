# 迭代：重复执行一组操作的过程，直到满足某个条件
# 迭代器：重复取值的工具
for i in range(10):
    print(i)
# l = ['a' , 'b' , 'c' ]
# num = 0
# while num < len(l):
#       print(l[num])
#       num += 1

# 字典 集合

# 选代器:不依赖索引也能迭代取值 __ next __ ()

# 可迭代对象特点 : 内置有 __ iter __ ()方法
# 可以转换为迭代器的对象就称为可迭代对象
# l = ['a' , 'b' , 'c' ]
# print(l .__ iter __ ())
# s1 ='张大仙'
# s1 .__ iter __ ()
# t = (1,2,3)
# t .__ iter __ ()
# d = {'key1' :1}
# d .__ iter __ ()
# s2 = {1,2,3}
# s2 .__ iter __ ()

d = {'key1':1,'key2' :2,'key3':3}
res = d.__iter__ ()
print(res is res.__iter__())
print(res)
while True:
    try:
        print(res.__next__())
    except StopIteration:
        break


"""
迭代器对象的特点:

1、内置 __ next __ (), __ iter __ ()方法
2、迭代器可以调用 __ iter __ 方法,得到的就是迭代器本身 这么设计是为了和for循环的工作原理统一起来
迭代器对象调用 __ next __ 方法,就会迭代器下一个值
可迭代对象不一定是迭代器对象
"""

"""
for循环工作原理:

                i = range(10) .__iter__ ()
                    try:
                        i.__next__()
                    except StopIteration:
                        break

                    i= (range(10).__iter__ ).__iter__ ()
                    try:
                        i.__next__()
                    except StopIteration:
                        break
"""


for i in range(10).__iter__():
    print(i)