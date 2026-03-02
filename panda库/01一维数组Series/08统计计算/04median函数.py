"""
    中位数
    Series.median(axis=0,skipna=True,numeric_only=False)
"""
import pandas as pd
import numpy as np
s1 = pd.Series([3,5,np.nan, 4,None])

print(s1.median())
