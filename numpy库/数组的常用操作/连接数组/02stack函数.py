"""
numpy.concatenate基于现有的轴进行数组的拼接
stack:总是会创建一个新的轴进行数组的拼接

numpy. stack(arrays, axis=0, out=None)
arrays:一系列数组,所有的数组必须具有相同的形状

假设你有N个数组,他们的形状都相同,比如都是(m,n)
np.stack 调用np.stack((a,b,c,…,n),axis=k)时,相当于在k的位置插入一个新的维度.
这个新维度的大小正好等于你堆叠的数组个数。
结果:如果你有N个(m,n)的数组,使用np.stack 后得到的数组形状将会是:
当k=0 (N,m,n)
当k=1 (m,N,n)
当k=2 (m,n,N)

"""
import numpy as np

# a = np.array([1, 2, 3])  # (3,)
# b = np.array([4, 5, 6])  # (3,)
#
# d = np.stack((a, b), axis=0)  # (2,3)
# print(d)
#
# d = np.stack((a, b), axis=1)  # (3,2)
# print(d)

arr1 = np.random.randint(5, size=(2, 2, 2))
arr2 = np.random.randint(5, size=(2, 2, 2))
print('数组1',arr1)
print('数组2',arr2)
arr3 = np.stack((arr1, arr2), axis=1)
print(arr3)
print(arr3.shape)
