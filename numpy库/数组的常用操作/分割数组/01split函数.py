"""
split:用于沿着指定的轴分割成多个数组
numpy.split(ary, indices_or_sections, axis=0)
ary:要分割的数组
indices_or_sections:

可以是一个整数,表示要将数组平分成多少个子数组
也可以是一个整数数组,表示分割的位置
axis:沿着哪个轴进行分割

"""

import numpy as np

# 1d 等分

# arr = np.arange(10)
# print('原数组:', arr)
#
# # 分成2个子数组
# result = np.split(arr, 2)
# print('分割结果:', result)
#
# # 1d 索引位置分割
#
# arr = np.arange(10)  # [0,1,2,3,4,5,6,7,8,9] arr[:3] arr[3:6] arr[6:]
# print('原数组:', arr)
#
# result = np.split(arr, [3, 6])
# print('分割结果:', result)
#
# # 2d 行方向分割
#
# arr = np.arange(12).reshape(4, 3)
# print('原数组:\n', arr)
#
# result = np.split(arr, 2, axis=0)
# print('分割结果:', result)
#
# result = np.split(arr, [1, 2], axis=0)
# print('分割结果:', result)
#
# # 2d 列方向分割
# result = np.split(arr, 3, axis=1)
# print('分割结果:', result)

#多维数组分割
result = np.random.randint(10, size=(2, 2, 4,3))
print('原数组:', result)
res = np.split(result, 2, axis=3)
print(res)
print(res[0].shape)