"""
    index:返回行索引
    columns:返回列索引
    values:返回数据
    dtype:返回每一列的数据类型
    shape:返回表格的形状
    size:元素个数
    empty:判断是否为空
    T:转置
    ndim:维度，默认为2
    attrs:存储元数据


"""

import numpy as np
import pandas as pd

data = {

    '编号': [1, 2, 3],
    '姓名': ['小明', '小刚', '小红'],
    '年龄': [20, 21, 19],
    '成绩': [78, 64, 89]
}
df = pd.DataFrame(data)
print(df)

print('行索引\n', df.index)
print('列索引\n', df.columns)
print('数据\n', df.values)
print('每一列的数据类型\n', df.dtypes)
print('表格的形状\n', df.shape)
print('数据的个数\n', df.size)
print('数据是否为空\n', df.empty)
print(df)
print('表格转置\n', df.T)
print('表格维度\n', df.ndim)

df.attrs = {'source': 'file', 'time': 'xx:xx:xx'}
print(df.attrs)
