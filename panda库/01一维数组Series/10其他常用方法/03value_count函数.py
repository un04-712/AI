"""
    用于计算Series中每个值出现的次数

    Series.value_counts(normalize=False, sort=True, ascending=False,bins=None, dropna=True)

    normalize:True返回每个值的相对频率，如果为'all'，则返回所有值相对频率之和为1
    sort:True按计算值降序排列
    ascending:True升序
    bins:用于离散化连续数据
    dropna:是否排除nan值
"""
import pandas as pd
import numpy as np

s = pd.Series([1,2,3,1,2,4,np.nan,2,4,5])

print(s.value_counts())