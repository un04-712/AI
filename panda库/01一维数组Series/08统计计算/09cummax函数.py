"""
    计算累计最大值
Series. cummax (axis=None, skipna=True, *args, ** kwargs)

应用场景: 股价走势
成绩分析
"""
import pandas as pd

s= pd.Series([2,1,3,5,4,6])

print(s.cummax())
