"""
    DataFrame.head(n=5)     默认返回5行
    DataFrame.tail(n=5)     默认返回最后5行
"""

import pandas as pd
data={
        '编号':[1,2,3],
        '姓名':['小明','小刚','小红'],
        '年龄':[20,21,19],
        '成绩':[78,64,89],
}
df = pd. DataFrame (data)
print(df)

print(df.tail(n=2))
print(df.head(n=2))