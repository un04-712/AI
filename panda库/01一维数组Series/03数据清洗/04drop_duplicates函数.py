"""
    去除series中对象中重复项
    Series.drop_duplicates()

    keep:决定如何处理重复项
        first:保留第一次出现的重复项
        last:保留最后一次的重复项
        False:不保留任何重复项
    inplace:是否在原series上进行修改
    ignore_index:如果为True，则索引被重置
"""

import pandas as pd
import numpy as np
series = pd.Series([100,99,77,77,99,33,33,33,np.nan,5])
print(series)
print(series.drop_duplicates())
print(series.drop_duplicates(keep='last'))
print(series.drop_duplicates(keep=False,ignore_index=True))
