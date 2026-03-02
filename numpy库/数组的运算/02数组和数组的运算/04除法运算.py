import numpy
import numpy as np
#矩阵的除法(矩阵对应元素相除)
arr1 = np.random.randint(10,size=(2,3))
print(arr1)
arr2 = np.random.randint(10,size=(2,3))
print(arr2)

print(arr1/arr2)

#函数运算       numpy.divide
print(np.divide(arr1,arr2))


# 生成两个2行3列的数组
arr1 = np.array([[11, 12, 13], [14, 15, 16]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# divide会使arr1中的每个元素除以arr2中的对应位置的元素
arr3 = np.divide(arr1, arr2)
print(arr1)
print(arr2)
print('运算的结果为：\n', arr3)