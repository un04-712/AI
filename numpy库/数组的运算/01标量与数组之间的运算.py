"""
    在numpy中，标量和数组的运算内部其实是以广播机制进行
    广播机制 :当标量和数组运算时,numpy会自动扩展标量的形状,使它们能够兼容并完成逐个元素的运算

"""
import numpy as np

arr1 = np.random.randint(3, 10, (2, 2))
print(arr1)
print(arr1 + 1)
print(arr1 - 1)
print(arr1 * 2)
print(arr1 / 2)
