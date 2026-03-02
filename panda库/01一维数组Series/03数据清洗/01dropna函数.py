"""
    03数据清洗：清洗series对象中某些值(nan)，对这些值进行修改和删除操作

    Series.dropna(axis=0,inplace=False)

    axis:参数支队datadrame有意义
    inplace:如果为True，则会直接在原series上删除缺失值，false则会返回删除了缺失值的新series，原series保持不变
"""

import pandas as pd
import numpy as np

series = pd.Series([1,np.nan,3,np.nan,5])

print(series)

print(series.dropna())