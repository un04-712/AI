"""
    shuffle:随机打乱数组元素
    numpy.random.shuffle(x)

    注意：
        shuffle函数只适用于一维数组
        shuffle函数只在原数组上进行，不会创建新的数组

"""
import numpy as np

a = np.arange(10)
print(a)
np.random.shuffle(a)

print(a)
