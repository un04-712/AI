"""
    使用布尔值进行索引

"""

import  numpy as np
import pandas as pd
data={
    '编号':[1,2,3],
    '姓名':['小明','小刚','小红'],
    '年龄':[20,21,19],
    '成绩':[78,64,89]
}
df = pd.DataFrame(data)
print(df)

print(df[df['成绩']>=60]['成绩'].count())