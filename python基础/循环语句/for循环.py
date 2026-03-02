"""
    for循环：
        for 临时变量 in 可遍历的对象：
            代码块

            应用场景：
            1.迭代器，遍历可迭代的对象
            2.有循环周期的场景，常常与range配合使用,临时变量在for循环完成之后依然能访问到的
range(start=0,stop,step=1)

"""
from itertools import count

#1、遍历数据
str1 = 'asdfghjkl'
list1 = [1,2,3,4,5,6,7,8,9]
ch = 2
for i in list1:
    print(i)
for i in str1:
    print(i)

#2、基本循环场景
#死循环
#for i in count():
 #   print(i)

#输出水仙花数的数量 每个位的三次方相加之后为数据本身
for i in range(1,1000):
    g = i % 10
    s = i // 10 % 10
    b = i // 100 % 10
    q = i // 1000 % 10

if(g**3+s**3+b**3+q**3) == i:
    print(f"{i}是水仙花数")





