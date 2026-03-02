"""
    列表推导式：
            new_list = [expression for item in iterable if condition]
            new_list = [expression for item in iterable]
            expression 是对item的操作或表达式，用于生成新的列表元素
            item 是可迭代对象中的元素，例如列表中的元素
            iterable 是用于迭代的可迭代对象，例如：列表、元组、集合等
            condition 是一个可选的条件，用于过滤元素。
"""
ls1 = [1,2,3,4,5]
#生成一个新的列表，要求列表里的元素是原始列表中每个元素的平方
#方法一
ls = []
for i in ls1:
    ls.append(i**2)
print(ls)
#方法二
ls1[::] = [1,4,9,16,25]
print(ls1)
#方法三 只取ls1中大于2的元素
ls2 = [item**2 for item in ls1 if item>2]
print(ls2)
#所有元素
ls2 = [item**2 for item in ls1 ]
print(ls2)







