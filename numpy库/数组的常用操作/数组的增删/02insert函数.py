
"""arr:原始数组
obj:插入位置的索引
values:要插入的值
"""
import numpy as np

# 插入单个值
arr = np.array([1,2,3,4,5])
print(arr)

result = np.insert(arr, 2, 10)

print(result)

# 多个值的插入
#在索引[1,3]的位置插入值[20,30]

result = np.insert(arr,[1,3], [20,30])
print(result)

# 沿着列方向取插入值
arr_2d = np.array([[1,2], [3,4], [5,6]])
print(arr_2d)