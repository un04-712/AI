"""
    重置索引    将原来的索引转换成一个列，并将一个新的默认整数索引返回给DataFrame

    DataFrame.reset_index(level=None, col_level=0,col_fill, drop=False, name=no_default, inplace=False, allow_duplicates=False)

    level:如果是多级索引，level表示要移除的级别，如果为None表示移除所有索引
    drop:True则表示不将旧索引添加为新列
    name:默认为no_default.
    col_level:如果原始索引是多级索引，则指定新列的索引规则
    col_fill:如果原始索引是多级索引，并且col_level比原始索引级别多，则使用此值填充缺失的级别
    inplace:是否在原数组上进行修改
    allow_duplicates:true表示允许在重置索引后出现重复索引

"""