"""
    randn:从标准的正态分布中抽取样本，返回的随机数将具有平均值为0，标准差为1的正态分布
    根据68-95-99.7规则

    68%的数据会落在平均值+-标准差       [-1,1]
    95%的数据会落在平均值+-2标准差       [-2,2]
    99.7%的数据会落在平均值+-3标准差       [-3,3]

    numpy.random.randn(d0,d1,d2……,dn)

"""
import numpy as np
print(np.random.randn(5))

print(np.random.randn(2,3))

