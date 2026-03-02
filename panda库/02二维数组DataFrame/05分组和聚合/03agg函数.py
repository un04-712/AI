"""
    允许有用一个或多个聚合函数到dataframe的列或行上,并返回聚合的结果
    Series.agg(func=None, axis=0, *args, ** kwargs)
    func:实际函数
    axis : 0 index 1 columns

"""
import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500],
    }
)

# 应用一个函数
print(df.agg('sum'))
# 应用多个函数
print(df.agg({'A': 'max', 'B': 'min', 'C': 'sum'}))
print(df.agg(['max', 'min', 'sum']))
print(df.agg({'A': 'max', 'B': 'min'}))
print(df.agg(['max', 'min']))
