"""
该函数的作用是创建指定形状、指定元素的数组,函数原型为:
numpy. full(shape, fill_value, dtype=None, order='C')

fill_value:用于填充数组的值

注意:如果fill_value不能转换成指定的dtype,则会引发错误

"""


import numpy as np
x = np. full ((2,3), 7)
print(x)
y = np. full ((2,3),7, dtype=float)
print(y)