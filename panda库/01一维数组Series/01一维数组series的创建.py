"""
    class pandas.Series(data=None,index=None,dtype=None,name=None,copy=None,fastpath=False)

    data :数据 可以为标量、列表、元组、字典、数组
    index:数组或列表，用于定义Series的索引，如果未提供您，则默认从0开始
    dtype:数组的数据类型
    name:series标识名，用于后续的索引和操作
    copy:布尔值，默认为false，尽可能避免复制数据，仅影响ndarray输入。如果为True,则复制数据，
    fastpath:布尔值，通常不用用户指定，内部优化标志，True：运行series构造函数绕过一些验证，加快series的创建速度
"""

import pandas as pd
from pandas import Series
import numpy as np

data = 20

s = pd.Series(data)
print(type(s))
print(s)

s = pd.Series(data, ('a', 'b', 'c'))
print(s)

"""
    列表方式
"""
s = pd.Series([60, 34, 99, 45, 54])
print(s)

"""
    字典方式创建
    字典的键是索引，字典的值就是该索引对应的值，如果用字典创建了series,并且指定了与字典键不同的index参数，那么生成的数组中的数据就是以index参数的值为索引，但索引的值是nan
    
    pandas:nan(not a number)  是一个特殊的浮点数，用于表示缺失数据或无效数据
"""

s = pd.Series({'A': 60, 'B': 34, 'C': 99, 'D': 45, 'E': 54}, [1, 2, 3, 'A', "E"])

print(s)

"""
    使用array创建一维数组
"""

s = pd.Series(np.array([1, 2, 3]), dtype='float64')
print(s)
