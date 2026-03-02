"""
    vstack:垂直堆叠
    numpy.vstack(tup)
    tup:一个数组序列，他们被垂直堆叠在一起，所有数组除了第1个轴以外必须具有相同的形状

"""

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.vstack((a, b))
print(c)
