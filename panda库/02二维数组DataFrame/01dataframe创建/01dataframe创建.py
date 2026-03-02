"""
class pandas. DataFrame (data=None, index=None, columns=None, dtype=None, copy=None)

    data:
        列表
        字典
        2d-ndarray
        Series
    index:行标签
    columns:列标签
    dtype:某列的数据类型,如果指定,则所有列都将转换为指定的数据类型
    copy:True则复制数据,False尽量不复制数据

"""
import numpy as np
import pandas as pd

#列表创建

df = pd.DataFrame([['小明', 90], ['小红', 86], ['小刚', 92]], columns=['姓名', '成绩'])
print(df)
"""
字典创建
"""

data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19]
}
df = pd.DataFrame(data)
print(df)

"""
ndarray创建
"""

data_array = np.array(
    [
        ['Tom', 20],
        ['Nick', 21],
        ['John', 19],
    ]
)
df = pd.DataFrame(data_array, columns=['姓名', '年龄'])
print(df)
"""
        series创建
"""

# 字典连接series
s1 = pd.Series(['小明', '小红', '小刚'], name='姓名')
s2 = pd.Series([20, 21, 19], name='年龄')
s3 = pd.Series([99, 76, 87], name=' 成绩')

df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
print(df)

# concat

df = pd.concat([s1, s2, s3], axis=1)

print(df)
