import numpy as np
#加法运算
arr1 = np.random.randint(5,size=(2,3))
print(arr1)
arr2 = np.random.randint(5,size=(2,3))
print(arr2)

arr3 = arr2-arr1
print(arr3)

#函数运算
"""
    numpy.subtract(x1, x2)
"""
# 生成两个2行3列的数组
arr1 = np.array([[11, 12, 13], [14, 15, 16]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# subtract会使arr1中的每个元素减去arr2中的对应位置的元素
arr3 = np.subtract(arr1, arr2)
print(arr1)
print(arr2)
print('运算的结果为：\n', arr3)