"""
    从dataframe中获取列，类似于直接使用df[key]来访问列，但是当列不存在时，get方法提供一个更安全的方式来处理这种情况，可以指定一个默认值，而不是抛出这个异常
    Dataframe.get(key, default=None)
    key:你想获取列的名称
    default:如果列不存在时返回的默认值,默认是None

"""

import pandas as pd

data = {
    '编号': [1, 2, 3],
    '姓名': ['小明', '小刚', '小红'],
    '年龄': [20, 21, 19],
    '成绩': [78, 64, 89]
}
df = pd.DataFrame(data)
print(df)
print(df.get('编号'))
print(df.get('身高'))
