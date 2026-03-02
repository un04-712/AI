"""
    用于检查DataFrame中元素是否包含在指定的集合values中，这个方法会返回一个布尔型的dataframe,其中每个元素都表示原始dataframe中对应的元素是否在values中

    DataFrame.isin(values)

    values:单个值 列表 元组 集合 dattaframe或者series 如果values是一个字典,键是列名，值就是列表或元组，表示该列中要检查的值

"""
import pandas as pd

data1 = {
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e']
}
data2 = {
    'A': [1, 2, 'e', 4, 5],
}
s1 = pd.Series([1, 2, 3, 4, 'a'])
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print(df1.isin([2, 4, 'c']))
print(df1.isin(df2))
print(df1.isin(s1))
