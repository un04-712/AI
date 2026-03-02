"""
    返回一个与原series长度相同的布尔型Series，其中对应的值为True表示该位置的元素在指定的值的集合
    中，false则表示不存在

    isin:用于判断Series中的每个元素是否在指定一组值中
    series。isin(values)
    values:可迭代对象，用于指定要判断的一组值

"""
import pandas  as pd
import numpy as np

#创建series对象
data = [1,2,3,4,5]

series = pd.Series(data,index=['a','b','c','d','e'])

#判断一组值是否在series中，并把满足条件的索引返回出来
print(series[series.isin([3]).values])

print(series.isin([3]).values)