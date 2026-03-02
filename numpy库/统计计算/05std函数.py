"""
    标准差 = 方差的平方根
    标准差作用：用来衡量数据的离散程度
    std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>)
"""

import numpy as np

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print('整个数组的标准差：', np.std(b))
print('数组每一列的标准差：', np.std(b, axis=0))
print('数组每一行的标准差：', np.std(b, axis=1))
