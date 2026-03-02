"""
    numpy.random,random(size=None)
    size:输出数组的形状，它可以是整数也可以是元组

"""

import numpy as np

a = np.random.random(3)
print(a)
b = np.random.random((3,2))
print(b)

"""
    rand 和 random的区别:
numpy.random.rand(d,d1, .. ,dn)需要一个或多个整数参数,这些参数 定义了返回数组的形状。例如,np.random.rand(2,3)会返回一个 2x3 的二维数组。
numpy.random.random(size=None)接受一个可选的可以是整数或者元组。如里size是一个数,它会返回一个一维数组,如果 size 是一个元组,它会返回一个多维数组
"""
