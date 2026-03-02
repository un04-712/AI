"""
    uniform:从均匀分布中抽取一个浮点数
    numpy.random.uniform(low=0.0,high=1.0,size=None)


"""
import numpy as np

#从0-10之间随机产生一个浮点数

print(np.random.uniform(10))

print(np.random.uniform(10,100))

print(np.random.uniform(10,100,(3,3,3)))

