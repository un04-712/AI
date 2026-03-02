"""
    替换特定的值
    Series.replace()

    to_place:要替换的值
        标量
        列表
        字典      键是指要替换的值，值是替换后的新值
        正则表达式:  regex=True
    value:替换后的值
    inplace:如果为True，则会直接在原series上删除缺失值，false则会返回删除了缺失值的新series，原series保持不变
    limit:表示最大替换量
    regex:是否启用正则表达式
    method:字符串  value为None该参数的值
        pad/ffill:用前一个非缺失值填充缺失值
        bfill/backfill:用后一个非缺失值填充缺失值
"""
import pandas    as pd
import numpy as np

"""
    
"""
s = pd.Series([1,2,3,4,4,3])

print(s.replace(2,20))

"""
    列表替换多个值
"""
print(s.replace([2,3],20))

"""
    字典替换值
"""

print(s.replace({2:20,3:20}))

"""
    正则表达式
"""

series = pd.Series(['apple','1banana','cheery','2apple pie','orange'])

#将包含有apple字符的值替换为fruit

print(series.replace(r'\d',value='fruit',regex=True))


"""
    method
"""
print(s.replace(2,method='ffill'))

