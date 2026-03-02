"""
    append:
    append(arr,values,axis=None)
    arr:原始数组
    values:要追加的值，values的形状必须与arr在除了要追加的轴之外所有轴上要兼容

"""
import numpy as np
arr = np.array([1,2,3])
result = np.append(arr,[1,2,3])
print(result)

arr = np.array([[1,2,3],[4,5,6]])
result = np.append(arr,[1,2,3])

