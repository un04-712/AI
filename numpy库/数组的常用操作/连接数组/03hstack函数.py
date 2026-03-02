"""
    hstack:水平堆叠
    numpy.hstack(tup)
    tup:一个数组序列，他们被水平堆叠在一起，所有数组除了第二个轴以外必须具有相同的形状

"""

import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[5, 6], [7, 8], [9, 10]])

c= np.hstack((a,b))
print(c)
# c = np.stack((a, b), axis=0)
# print(c)
# print(c.shape)
