"""
    index:          返回Series中的索引  可读可写
    values:         返回series中的值  可读
    name:           返回series的名称    可读可写
    dtype和dtypes    对于series来说，两个属性的作用是一样的，都是用来查看series对象的数据类型
    shape:          返回series的形状
    size:           返回元素数量
    empty:          返回数组是否为空
    hasnans:        判断元素中是否存在nan值，如果有则返回true
    is_unique:      判断是否有重复元素，如果有则返回false,没有则返回True
    nbytes:         返回数据所占的字节数
    axes:           返回series行标签的列表
    ndim:           返回series的维度
    array:          返回series的底层数组，包括数组的元素、长度、数据类型
    attrs:          返回series自定义的属性，可以存储额外的说明性属性
    is_monotonic_decreasing     判断是否按照降序排列
    is_monotonic_increasing     判断是否按照升序排列
"""

import pandas as pd

series = pd.Series({'data': '2025-2-10', 'weight': 50, 'height': 182})

print('索引:', series.index)
print('值:', series.values)
print('类型:', series.dtypes)
print('形状:', series.shape)
print('元素数量:', series.size)
print('是否为空:', series.empty)

print('是否存在nan值:', series.hasnans)
print('是否存在重复元素:', series.is_unique)
print('所占字节数:', series.nbytes)
print('返回行标签的列表:', series.axes)
print('返回数组的维度:', series.ndim)
print('是否为降序排列:', series.is_monotonic_decreasing)
print('是否为升序排列:', series.is_monotonic_increasing)
