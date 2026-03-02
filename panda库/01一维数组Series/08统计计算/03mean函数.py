"""
    Series.mean(axis=0,skipna=True,numeric_only=None)
    axis:沿看哪个轴方问进行计算
    skipna;跳过NaN值
    numeric_only:为True则只对数字类型进行运行
"""


import pandas as pd
import numpy as np
s1 = pd.Series([3,5,np.nan, 4,None])

print(s1.mean())