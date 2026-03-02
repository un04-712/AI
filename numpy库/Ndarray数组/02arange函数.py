"""
    num.py
    arange([sttop[art,] s,step,],dtype=None,*,like=None)
"""
import numpy as np
 # 创建一个0-9的数组
arr1 = np.arange(10)
print(arr1)
# 创建一个5-14的数组,步长为2
arr2 = np.arange(5,15,2)
print(arr2)
# 创建一个0-1的数组,步长为0.1
arr3 = np.arange(0,1,0.1)
print(arr3)

# 创建一个0-9的数组,类型变为浮点数
arr4 = np.arange(10,dtype=np.float32)
print(arr4)
print(type(arr4))