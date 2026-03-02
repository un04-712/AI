"""
    var:求数组的方差
    方差的作用：用来衡量数据集的离散程度的一个统计量，方差越大表示数据波动越大，方差越小，表示数据越集中
    var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>)
     标准差 = 方差的平方根
     标准差作用：用来衡量数据的离散程度
"""
import numpy as np
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print('整个数组的方差：',np.var(b))
print('数组每一列的方差：',np.var(b,axis=0))
print('数组每一行的方差：',np.var(b,axis=1))