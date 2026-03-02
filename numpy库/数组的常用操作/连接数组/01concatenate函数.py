"""
concatenate:将多个数组沿指定的轴连按起来,形成一个更大的数组
numpy. concatenate((a1, a2, ... , arr_n), axis=0, out=None)
注意:(a1,a2,…,arr_n)这些要拼接的数组必须满足除了连接轴之外的所有维度的长度需要相同


"""

import numpy as np

a = (np.arange(4) + 1).reshape(2, 2)
print('a:\n', a)
b = np.array([[5, 6]])
print('b:\n', b)
# 水平拼接
c = np.concatenate((a, b.T), axis=1)
print('c:\n', c)
# 垂直拼接
d = np.concatenate((a, b), axis=0)
print('d:\n', d)
