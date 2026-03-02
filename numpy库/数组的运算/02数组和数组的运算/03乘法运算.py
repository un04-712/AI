import numpy
import numpy as np
#矩阵的点乘(矩阵对应元素相乘)
arr1 = np.random.randint(10,size=(2,3))
print(arr1)
arr2 = np.random.randint(10,size=(2,3))
print(arr2)

print(arr1*arr2)


#函数运算

print(np.multiply(arr1,arr2))

#标准矩阵乘法  Amn * Amp = Amp
"""
    numpy.dot(a,b,out = None)
"""
rr1 = np.random.randint(10,size=(2,3))
print(arr1)
arr2 = np.random.randint(10,size=(3,2))
print(arr2)
print(np.dot(arr1,arr2))


