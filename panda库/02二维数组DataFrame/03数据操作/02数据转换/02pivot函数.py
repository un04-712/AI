"""
    用来改变表格形状
    DataFrame.pivot(columns,index,values)

    colnumns:作为新DataFrame的行索引的列名，可以是单个列名或列名列表
    index:作为新DataFrame的列索引的列名，可以是单个列名或列名列表
    values:作为新DataFrame的值的列名，可以是单个列名或列名列表
"""

import pandas as pd

df = pd. DataFrame(
{
'日期':['2021-01-01','2021-01-01','2021-01-02','2021-01-02'],
'城市':['广州','长沙','广州','长沙'],
'温度':[5,20,3,22],
'湿度':[80,10,75,8]
})
print(df)

newdf=df.pivot(index='日期',columns='城市',values=['温度','湿度'])

print('行标签\n',newdf.index)
print('列标签\n',newdf.columns)
print('值\n',newdf.values)
print(newdf)