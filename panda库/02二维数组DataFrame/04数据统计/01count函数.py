"""
    计算DataFrame中非None值的数量
    Data.Frame(axis=0,numeric_only=False)

    axis:
        0 则对每行进行计数
        1 则对每列进行技术
    numeric_only:

"""
import pandas as pd
import numpy as np

df = pd. DataFrame (
    {
        'A':[1,2,np.nan, 4],
        'B':[5,np.nan,np.nan, 8],
        'C' : [ 'foo' , 'bar' , 'baz' , np. nan]
    }
)
print(df)
# 计算每列的个数
print(df.count())
print(df.count(numeric_only=True))

# 计算每行的个数
print(df.count(axis=1))