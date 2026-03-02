"""
    方差
        Series. var(axis=None, skipna=True,ddof=1, numeric_only=False)

        ddof: Delta Degress of freedom(自由度调整)用于贝塞尔矫正 以得到样本方差的估计
对于无偏估计(样本方差)

        样本方差:从样本中估计估计总体的误差
        总体方差: 计算总体的误差
        ddof通常设置为1 如果计算总体方差 应该把ddof设置为0
"""
import pandas as pd
import numpy as np

s1 = pd. Series([3,5,np.nan,4, None])

print(s1.var(ddof=0))