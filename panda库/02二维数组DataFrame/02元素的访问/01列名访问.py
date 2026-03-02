"""
    ['列标签']
"""

import pandas as pd

data = {
    '编号': [1, 2, 3],
    '姓名': ['小明', '小刚', '小红'],
    '年龄': [20, 21, 19],
    '成绩': [78, 64, 89]
}
df = pd.DataFrame(data)
print(df['姓名'][0])

print(df[['姓名', '成绩']])
