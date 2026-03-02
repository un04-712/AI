"""
    ndarray数组使用[]进行索引，从左到右从0开始，从右到左从-1开始
"""

import numpy as np
#一维数组的索引
arr = np.array([1,2,3,4,5])

print(arr[0])
print(arr[-1])
print(arr[2])

print('*'*66)
#创建二维数组
a = ([[1,2,3],[3,4,5]])
a = np.array(a)
#多维数组的索引
#只有一个索引指标时，会在第0维度上索引，后面的维度保持不变
print(a[0])

#两个索引指标
print(a[0][0])
print(a[1][2])
print(a[0,2])

print('*'*66)
#一维数组的切片

arr = np.arange(10)
print(arr[4:7])
print(arr[1:6:2])
arr[4:8] = 7
print(arr)

#高维数组的切片
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

"""
行切片
"""


# 选择连续的多行
# 取2,3行内容
print(a[1:])
print(a[1:3])
# 选择不连续的多行
# 取1,3行内容
print(a[0:3:2])
print(a[[0,2]])

print('*'*69)
"""
列切片
"""
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])

# 取出第二列
print(arr[:,1])

# 选择连续的多列
# 取2,3列内客
print(arr[:,1:])

# 选择不连续的多列
# 取1,3列内容
print(arr[:, :: 2])
print(arr[:, [0,2]])
print('*'*69)
"""
同时选择行和列
"""


# 取出 2×2 2×3 3×2 3×3

# print(arri[[1,2], [1,2]])
print(arr[1:3,1:3])