"""
    标签访问
            series[标签名] 优先级：标签索引大于位置索引


"""
import pandas as pd
import numpy as np

series = pd.Series(np.arange(5),index=['a','b','c','d','e'])
print(series)

print(series['b'])  #标签访问
print(series[1])    #位置访问

"""
    函数实现位置访问和标签访问
"""
print(series.iat[1]) #下标访问
print(series.at[2]) #标签访问
