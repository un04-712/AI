import numpy as np
arr1 = np.random.randint(5,size=(2,3))
print(arr1)
arr2 = np.random.randint(5,size=(2,3))
print(arr2)

arr3 = arr2+arr1
print(arr3)

"""
    函数运算：numpy.add(x1, x2, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True)

    x1: 第一个输入数组或标量。
    x2: 第二个输入数组或标量。
    out: 输出数组，数据类型必须与预期输出相符。如果提供，它必须具有与输出 相同形状的适当类型来接收结果。
    where: 表示计算加法的条件，如果设置为True，则在相应位置进行计算；如果 设置为False，则在相应位置不进行计算。
    casting: 定义如何处理数据类型转换，例如 ‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’。
    order: 指定结果的内存布局，‘C’ 表示 C 风格，‘F’ 表示 Fortran 风格，‘A’
     表示原 数组样式，‘K’ 表示元素在内存中的出现顺序。
    dtype: 指定输出数组的类型。
    subok: 控制返回数组是否可以是输入数组的子类。
            
"""
# 生成两个2行3列的数组
arr1 = np.array([[11, 12, 13], [14, 15, 16]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# add会使arr1和arr2中的每个对应位置的元素相加
arr3 = np.add(arr1, arr2)
print(arr1)
print(arr2)
print('运算的结果为：\n', arr3)