"""
    normal：从具有指定平均值和标准差的正态分布中抽取样本
    numpy.random.normal(loc=0,scale=1.0,size=None)
    loc:正态分布的均值
    scale:标准差
    size：输出数组的形状，它可以是整数也可以是整数元组

"""
import numpy as np

print(np.random.normal())

#均值为3，标准差为2
"""
根据68-95-99.7规则

    68%的数据会落在平均值+-标准差       [1,5]
    95%的数据会落在平均值+-2标准差       [-1,7]
    99.7%的数据会落在平均值+-3标准差       [-3,9]
"""

print(np.random.normal(3,2,(3,3)))
