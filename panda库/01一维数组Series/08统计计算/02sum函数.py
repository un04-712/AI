"""
    计算所有值的和

"""

import pandas as pd
import numpy as np
s1 = pd.Series([1,5,np.nan, 4,None])

# np.nan * np.int5*
print(1+np.nan)
print(1*np.nan)
print(1/np.nan)

print(1/np.inf)
print(-1*np.inf)
print(-1+np.inf)
print(-np.inf*np.inf)

print(s1.sum(skipna=False))