"""
    join()：用于将两个对象的列连接起来。
    DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='',sort=False, validate=None)
    other : 另一个 DataFrame 对象。
    on : 用于连接的列名。
    how : {‘left’, ‘right’, ‘outer’, ‘inner’}, 默认为 ‘left’。确定连接的类型：
        ‘left’: 使用左侧（调用 join 的 DataFrame）的索引进行左连接。
        ‘right’: 使用右侧（参数 other 中的 DataFrame）的索引进行右连接。
        ’outer’: 使用两个 DataFrame 的索引的并集进行全外连接。
        ‘inner’: 使用两个 DataFrame 的索引的交集进行内连接。
    lsuffix : 用于重命名重复列的左后缀。默认值为空字符串 '' 。
    rsuffix : 用于重命名重复列的右后缀。默认值为空字符串 '' 。
    sort : 是否对结果进行排序。默认值为 False 。
    validate : 检查合并键。可以是：
        'one_to_one' ：检查合并键在两者中是否唯一。
        'one_to_many' ：检查合并键在左侧是否唯一。
        'many_to_one' ：检查合并键在右侧是否唯一。
        'many_to_many' ：不检查。
"""













