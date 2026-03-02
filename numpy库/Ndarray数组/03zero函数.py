"""
    zero(shape,dtype=float,order='C',*,like=None
    shape:一个整数/整数元组，可以指定输出数组的形状
"""
import numpy as np

# 创建一个一维全零数组
arr1 = np.zeros(5)
print(arr1)

#创建一个二维全零数组
arr2=np.zeros((3,2))#3行两列的数组
print(arr2)

# 创建一个三维全零数组
arr2= np.zeros((3,2,4))#3x2x4形状的数组
print(arr2)

#创建一个四维数组
arr3= np.zeros((3,2,4,5))#3x2x4x5形状的数组
print(arr3)
