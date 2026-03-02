"""
    筛选出满足条件的值
"""

import pandas as pd
import numpy as np

series = pd.Series(np.random.randint(0,100,(50,)))
print(series[series>60])