"""
    DataFrame.merge()：用于根据一个或多个键将两个 DataFrame 对象连接起来。
    DataFrame.merge(right, how='inner', on=None, left_on=None,right_on=None, left_index=False, right_index=False, sort=False,suffixes=('_x', '_y'), copy=None, indicator=False, validate=None)

    right : 另一个 DataFrame 对象。
    how : {‘left’, 'right', 'outer', 'inner', 'cross'}, 默认为 'inner'。确定连接的类型：
         'left': 使用左侧（调用 merge的 DataFrame）的索引进行左连接
         'right': 使用右侧（参数 right 中的 DataFrame）的索引进行右连接。
         'outer': 使用两个DataFrame的并集连接。
         'inner': 使用两个DataFrame的交集连接。
    on : 用于合并的列名。如果 left_on 和 right_on 都没有指定，则使用 on 。
        left_on : 左侧 DataFrame 中用于合并的列名。不与on同时使用。
        right_on : 右侧 DataFrame 中用于合并的列名。不与on同时使用.
    left_index : 是否使用左侧 DataFrame 的索引作为合并键。默认值为 False 。不与on同时使用。
    right_index : 是否使用右侧 DataFrame 的索引作为合并键。默认值为False 。不与on同时使用。
    sort : 是否对结果进行排序。默认值为 False 。
    suffixes : 用于重命名重复列的后缀。默认值为 ('_x', '_y') 。
    copy : 是否复制数据。默认值为 None ，表示根据需要自动决定是否复制。
    indicator : 是否添加一个指示器列，显示每行来自哪个 DataFrame 。默认值为False 。
    validate : 检查合并键。可以是：
    'one_to_one':检查合并键在两者中是否唯一。
    'one_to_many':检查合并键在左侧是否唯一。
    'many_to_one':检查合并键在右侧是否唯一。
    'many_to_many':不检查。
"""
import pandas as pd
import  numpy as np