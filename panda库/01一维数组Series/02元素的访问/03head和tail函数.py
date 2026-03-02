""""
    head:快速查看series数据开头的部分内容
    tail:快速查看series数据末尾的部分内容
    series.head(n=None)
    series.tail(n=None)

    n: None:值为5 指定要返回的行数
"""
import pandas as pd
import numpy as np

series = pd.Series(np.random.rand(20))
print(series.head(5))
print(series.tail(3))