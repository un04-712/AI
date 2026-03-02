"""
    用于删除dataframe中重复的行
    Dataframe. duplicates(subset=None,keep='first',inplace=False,ignore_index=False)

    subset:表示要检查重复的列名或列名列表  默认为none,检查所有列
    keep:
        first:保留第一次出现的

        last:保留最后一次出现的

        False:不保留
    inplace:是否在原dataframe中做修改
    ignore_index:是否重置索引
"""
import pandas as pd
import numpy as np
data={
'编号':[2,np.nan,2],
'姓名':[2,'小刚',2],
'年龄':[2,np.nan,2],
'成绩':[2,64,2]
}
df = pd.DataFrame (data)
print(df)
print(df.drop_duplicates())

print(df.drop_duplicates(subset=['编号']))
