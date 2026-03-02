"""
    方差
        DataFrame.var(axis=None, skipna=True,ddof=1, numeric_only=False)

        ddof: Delta Degress of freedom(自由度调整)用于贝塞尔矫正 以得到样本方差的估计
对于无偏估计(样本方差)
        axis
        样本方差:从样本中估计估计总体的误差
        总体方差: 计算总体的误差
        ddof通常设置为1 如果计算总体方差 应该把ddof设置为0
"""
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': [43, 2, 43, np.nan]
    }
)
print(df)
print(df.var(ddof=0, numeric_only=True))
