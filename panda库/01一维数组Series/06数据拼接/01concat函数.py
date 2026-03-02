"""
    用于将多个pandas对象(series dataframe)沿着一个连接起来
    pandas.concat(objs,)

    objs:参与连接的pandas对象的列表或元组
    axis:轴
    join:outer表示并集  inner表示交集(只在dataframe中有效)
    ignore_index:
    keys:序列，用于构造分层索引的键
    levels:序列列表，用于构造分层索引特定的键

    sort:
    copy:为None表示自动选择，True:拷贝底层数据,为false尽量不拷贝
"""

import pandas as pd

import  numpy as np
s1 = pd.Series(np.random.randint(0,5,(5,)))
s2 = pd.Series(np.random.randint(20,50,(5,)))
s3 = pd.Series(np.random.randint(60,100,(5,)))

print(pd.concat([s1,s2,s3]))