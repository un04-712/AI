"""
    DataFrame.mean(axis=0,skipna=True,numeric_only=None)
    axis:沿看哪个轴方问进行计算
    skipna;跳过NaN值
    numeric_only:为True则只对数字类型进行运行
"""
import pandas as pd
import numpy as np
df = pd. DataFrame (
    {
        'A':[1,2,np.nan, 4],
        'B':[5,np.nan,np.nan, 8],
        'C' : [ 'foo' , 'bar' , 'baz' , np. nan]
    }
)
print(df)
print(df.mean(numeric_only=True))
print(df.mean(axis=1,skipna=False,numeric_only=True))