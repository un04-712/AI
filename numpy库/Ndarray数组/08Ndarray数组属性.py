"""
    shape；返回一个表示数组大小的元组
    dtype：数组元素的数据类型
    size： 元素的个数
    ndim： 数据维度的大小，其大小等于调用shape返回的元组个数

"""
import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.shape)
print(a.dtype)
print(a.size)
print(a.ndim)