"""
    array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
          like=None)
    object:为可迭代对象，表示要转换为数组的数据
    dtype:可以指定数组的数据类型，如果未指定，根据输入数据自动推断
    copy:如果为True,则复制输入数据，如果为False则有必要时才复制。如果object已经是一个numpy数组
    并且满足其他条件(dtype,order等)在，则不会进行复制
    order:C(行优先)，F(列优先)，
"""

import numpy as np


#创建一维数组
a = np.array([1,2,3])
print(type(a))
print(a)

#创建二维数组
a = np.array([1,2,3])

"""
    copy参数示例
"""
#copy=True,强制复制数据
b = np.array([1,2,3])
c = np.array(b,copy=True)
c[0] = 100
print(b)
print(c)

#copy=False,有必要时复制数据
b = np.array([1,2,3])
c = np.array(b,copy=False)
c[0] = 10
print(b)
print(c)
