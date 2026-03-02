import numpy as np
"""
    numpy的特点:
        1、Ndarray数组所有元素的数据类型相同、数据地址连续,
        批量操作数组元素时速度更快,而list中元素的数据类型可能不同,需要通过寻址的方式找到下一个元素。
        2、Ndarray数组支持广播机制,矩阵运算时不需要写for循环。
        3、底层主要使用C语言实现,运行速度远高于Python代码。
"""


a = [1,2,3,4,5]
for i in range(len(a)):
    a[i] += 1
print(a)



a = np.array([1,2,3,4,5])
a += 1
print(a)

#2.两个向量相加

a = [1,2,3,4,5]
b = [5,4,3,2,1]
c = [0,0,0,0,0]

for i in range(len(a)):
    c[i] = a[i]+b[i]

print(c)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([5,4,3,2,1])
print(arr1+arr2)