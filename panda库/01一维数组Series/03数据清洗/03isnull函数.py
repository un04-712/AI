"""
    检测series对象中的缺失值，他会返回一个布尔型的series，其中灭个元素都表示原series对应的位置是否为缺失值

    series.isnull()
"""

import pandas as pd
import numpy as np
series = pd.Series([100,np.nan,99,np.nan,5])

print(series.isnull())
