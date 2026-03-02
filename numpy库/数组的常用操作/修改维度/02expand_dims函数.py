"""
    在指定的位置增加一个单一维度，即在指定位置增加一个形状为1的维度
    numpy.expand_dims(a,axis)

"""
import numpy as np

arr = np.array([1,2,3])
print(arr)
print(np.expand_dims(arr,0))
print(np.expand_dims(arr,1))