"""
    计算累计乘积
    dataframe. cumprod(axis=0, skipna=True, *args, ** kwargs)

    应用场景: 股价走势
            成绩分析

"""


import pandas as pd
import numpy as np

df = pd. DataFrame(
    {
        'A':[1,2,np.nan,4],
        'B':[5,np.nan, np.nan, 8],
        'C':[43,2,43,np.nan]
    }
)
print(df)
print(df.cumprod())