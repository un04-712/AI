"""
    标准差
    DataFrame.std(axis=0,skipna=True,ddof=1,numeric_only=False，**kwargs)
"""
import pandas as pd
import numpy as np

df = pd. DataFrame(
    {
        'A':[1,2,np.nan,4],
        'B':[5,np.nan, np.nan,8],
        'C':[43,2,43,np.nan]
    }
)
print(df)
print(df.std(ddof=0,numeric_only=True))
print(df.std(axis=1,skipna=True,ddof=1,numeric_only=True))