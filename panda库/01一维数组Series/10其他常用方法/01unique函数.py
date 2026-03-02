"""
    返回一个数组，其中包含series中唯一的值，数组的值是按照他们在原始series中首次出现的顺序排列的
    Series.unique()
"""

import pandas as pd
s = pd.Series([1,2,3,1,2,4,3,2,4,5])

print(s.unique())