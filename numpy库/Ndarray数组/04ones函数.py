"""
numpy. ones(shape, dtype=float, order='C')

"""


import numpy as np

# 创建一个一维全1数组
arr1 = np.ones(5)
print(arr1)

# 创建一个二维全1数组
arr2=np.ones((3,2))#3行两列的数组
print(arr2)

# 创建一个三维全1数组
arr3 = np.ones((3,2,4))#3x2x4形状的数组
print(arr3)