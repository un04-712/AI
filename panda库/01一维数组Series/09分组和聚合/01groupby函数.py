
"""
    用于将series中数组分组,并允许对这些分组进行操作,比如计算每个组的总和,平均值,最大值等
    Series.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True)

    by:确定分组依据,如果by是一个函数,它会在对象索引的每个值上调用,入股传递了字典或series,将使用这些对象的值来确定组。如果传递了
    长度等于所选轴的列表或ndarray,则直接使用这些值来确定组
    axis
    level:用于指定分组所依据的级别
    as_index:是否将分组键作为结果的索引 仅于dataframe有关
    sort:是否对结果进行排序
    group_keys:是否包含分组键
    observed:是否仅包含实际观察到的分类值
    dropna:是否从结果中排除包含nan的组
"""
# 按相同的值来分组
import pandas as pd
import numpy as np
print('按值来分组 =====')
data = [10,20,10,30,20,10]
series = pd.Series(data)

grouped = series.groupby(series)

print(list(grouped))
print(grouped.count())
print(grouped.sum())

# 按列来分组
print('按标签来分组 =====')
data = [10,20,30,40,50,60]
index = ['a','b','a', 'b','c', 'c']
series = pd.Series(data, index=index)

grouped = series.groupby(series.index)
print(list(grouped))

# 二级索引下的分组
print('按二级索引来分组 ==:')

arrays = [np.array(['qux', 'qux', 'foo', 'foo',
                    'baz', 'baz', 'bar', 'bar']),
          np.array(['two', 'one', 'two', 'one',
                    'two', 'one', 'two', 'one']) ]
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=arrays)
res = s.groupby(level=0, sort=False)
print(list(res))
res = s.groupby(level=0).count()
print(res)

