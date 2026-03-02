"""
    复制Series对象
    Series.copy(deep=True)
    deep:True   深拷贝
"""
import pandas as pd
import numpy as np

s = pd.Series([1,2,3,1,2,4,np.nan,2,4,5])

