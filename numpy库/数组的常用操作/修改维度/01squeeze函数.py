"""
    squeeze:从函数形状中删除所有单维度的条目
    简单来说，就是把形状为1的维度去掉
    numpy.squeeze(a,axis=None)

    axis:一个整数或者元组，如果指定了该参数，则只压缩指定的轴，如果该轴不是单维度，则不会进行压缩
"""
import numpy as np

arr = np.array([[[1], [2], [3]]])
print(arr)
print(arr.shape)

# 对所有的轴全部进行压缩
squArr = np. squeeze (arr)
print (squArr.shape)
# 对0轴进行压缩
squArr = np.squeeze(arr,axis=0)
print(squArr. shape)
# 对1轴进行压缩
squArr = np.squeeze(arr,axis=1)
print(squArr. shape)