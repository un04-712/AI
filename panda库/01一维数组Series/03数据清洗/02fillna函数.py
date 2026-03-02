"""
    填充nan的值

    Series.fillna()

    value:用于填充缺失值的标量或字典，如果传递的是字典，则字典的键就是填充的标签，值用于填充的值

    method:字符串
        pad/ffill:用前一个非缺失值填充缺失值
        bfill/backfill:用后一个非缺失值填充缺失值

    axis:只对dataframe有意义
    inplace:如果为True，则会直接在原series上删除缺失值，false则会返回删除了缺失值的新series，原series保持不变
    downcast:用于转换数据类型 字符串
"""

import pandas as pd
import numpy as np

series = pd.Series([100,np.nan,99,np.nan,5])

print(series)
#标量填充
print(series.fillna(-1))
#前向填充
print(series.fillna(method='ffill'))
#后向填充
print(series.fillna(method='bfill'))
#标签填充

filled_with_spec = series.fillna({1:20,3:30})
print(filled_with_spec)

"""
    limit
"""
print(series.fillna(-1,limit=1))

"""
    downcast
"""
print(series.fillna(-1,limit=1,downcast='float16'))
