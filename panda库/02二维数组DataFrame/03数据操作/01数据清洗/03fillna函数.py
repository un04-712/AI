"""
    DataFrame.fiina(value=None,Method=None,axis=0,inplace=False,limit=None)
    value:标量，字典 series
    method；
        pad/ffill:用前一个非缺失值填充缺失值
        bfill/backfill:用后一个非缺失值填充缺失值
    axis:轴
    inplace:是否修改原始dataFrame
    limit：限制连续填充的数量



"""

import  numpy as np
import pandas as pd
data={
    '编号':[np.nan,np.nan,np.nan],
    '姓名':['小明','小刚','小红'],
    '年龄':[20,np.nan,19],
    '成绩':[78,64,89]
}
df = pd.DataFrame(data)
print(df)

"""
    标量填充
"""

print(df.fillna(2))

"""
    前向填充
"""
print(df.fillna(method='ffill',axis=1))

"""
    后向填充
"""
print(df.fillna(method='bfill',axis=0))

"""
    指定列标签填充
"""
data={
    '编号' :- 1,
    '姓名':'xxx',
    '年龄' :- 1,
    '成绩':0
}

print(df.fillna(value=data))


"""
    limit限制填充个数
"""
print(df.fillna(value=data, limit=1))