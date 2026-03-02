"""
计算累计和
Series. cumsum (axis=None, skipna=True, *args, ** kwargs)

        应用场景:股价走势
                成绩分析


"""

import pandas as pd

S= pd.Series([2,1,3,5,4,6])


print(S.cumsum())
