"""
    标准差
    Series.std(axis=0,skipna=True,ddof=1,numeric_only=False，**kwargs)
"""
import pandas as pd
import numpy as np

s1 = pd. Series([3,5,np.nan,4, None])

print(s1.std(ddof=1))