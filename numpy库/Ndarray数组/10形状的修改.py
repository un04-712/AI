import numpy as np

"""
    作用：用于给数组一个新的形状不改变其数据，返回的是一个新的数组
    如果给定的形状与原始数据不兼容会报错
    reshape(newshape,order='C')
"""
a = np.full((2,3),6)
b = a.reshape((3,2))
print(a)
print(b)

"""
    resize:用于改变数组的大小，他会直接修改调用原始数组，如果形状大于原始数组，则会在数组末尾添加元素，这些元素尚未定义
    如果新的形状，小于原始形状，则会截断数组
    numpy.ndarray.resize
"""
a = np.full((3,3),6)
print(a)
a.resize((2,1))
print(a)
a.resize((5,5))
print(a)

"""
    flatten:返回一个一维数组，它是原始数组的拷贝，默认为行顺序展平，可以通过参数order来指定展平的顺序
    numpy.ndarray.flatten(order='C')
"""
import numpy as np
arr1 = (np.arange(6)+1).reshape((3,2))
print(arr1)

"""
    ravel:返回的是一个连续的数组，他尝试以最低的复制操作来返展平后的数组
    numpy.ndarray.ravel(order='C')
"""
import numpy as np
arr1 = (np.arange(6)+1).reshape((3,2))
arr2 = arr1.ravel()
print(arr1)
"""
flatten方法返回的是原始数组的副本，这意味着返回的新数组与原始数组是两个独立的对象，对新数组的修改不会影响原数组
ravel方法返回的是视图或副本，这取决于数组的顺序，如果数组是连续的则ravel返回的是视图。如果数组是不连续的则返回的是副本
"""

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.flatten()
c = a.ravel()
d = a.ravel(order='F')
a[0][0] = 100
print('a', a)
print('b', b)
print('c', c)
print('d', d)