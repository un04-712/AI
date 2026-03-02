"""
    重置索引    将原来的索引转换成一个列，并将一个新的默认整数索引返回给series

    Series.reset_index(level=None, *, drop=False, name=no_default, inplace=False, allow_duplicates=False)

    level:如果是多级索引，level表示要移除的级别，如果为None表示移除所有索引
    drop:True则表示不将就所以添加为新列
    name:默认为no_default.
    inplace:是否在原数组上进行修改
    allow_duplicates:

"""