"""
    计算Series中非缺失值的个数

"""

import pandas as pd
import numpy as np

s1 = pd.Series([1,5,np.nan,None])


print(s1.size)
print(s1.count())