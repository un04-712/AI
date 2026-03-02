"""

计算所有值的和
    DataFrame.sum(axis=0, skipna=True, numeric_only=None)
    axis:沿着哪个轴方向进行计算
    skipna ; 跳过NaN值
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
# 计算每列的总和
print(df.sum(numeric_only=True))
# 计算每行的总和
print(df.sum(axis=1,numeric_only=True))
