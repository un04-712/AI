"""
    用于计算DataFrame中每个值出现的次数

    DataFrame.value_counts(subset,normalize=False, sort=True, ascending=False, dropna=True)
    subset:指定要进进行计算操作的列名列表
    normalize:True返回每个值的相对频率，如果为'all'，则返回所有值相对频率之和为1
    sort:True按计算值降序排列
    ascending:True升序
    bins:用于离散化连续数据
    dropna:是否排除nan值
"""