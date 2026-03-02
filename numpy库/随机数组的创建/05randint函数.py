"""
    randint:生成随机整数,指定范围的均匀分布
    numpy.random.randint(low,high=None,size=None,dtype=int)
    low(包含)：随机数的起始点，如果提供low没提供high，那么随机整数的范围从0-low(不包含low本身)
    high(不包含)：随机数的结束点

"""

import numpy as np
#从0-10之间随机产生一个整数

print(np.random.randint(10))

print(np.random.randint(10,100))

print(np.random.randint(10,100,(3,3,3)))

print(np.random.randint(10,100,(3,3,3),dtype=np.int32))
