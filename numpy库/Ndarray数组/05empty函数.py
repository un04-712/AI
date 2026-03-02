"""
该函数的作用就是创建一个指定形状、数据类型且未初始化的数组,函数原型是:
numpy. empty (shape, dtype=float, order='C')

注意:empty不初始化数组元素,因此它比numpy.ones更快,但数组中的值是未定义的,可能包含任何值
在使用numpy.zeros或 numpy.empty创建数组后,应有效填充数组,以避免使用未定义的数据快

"""


import numpy as np
x = np.empty(10)
print(x)


x = np.empty ( 10,dtype=int)
print(x)