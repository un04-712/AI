"""
    计算Series中唯一值的数量
    Series.nunique(dropna)

    dropna:布尔值，为true会排除缺失值,默认为True
"""

import pandas as pd
import numpy as np
s = pd.Series([1,2,3,1,2,4,np.nan,2,4,5])

print(s.unique())

print(s.nunique())