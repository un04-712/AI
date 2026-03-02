"""
    中位数
    DataFrame.median(axis=0,skipna=True,numeric_only=False)

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
print(df.median(numeric_only=True))
print(df.median(axis=1,numeric_only=False))