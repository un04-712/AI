"""
    DataFrame.melt(id_vars=None, value_vars=None,
var_name=None, value_name='value', col_level=None, ignore_index=True)

    id_vars:保持不变的列名列表
    values_index:字符串或字符串列表，要重塑的列名或列名列表，这些列的值将被展平到新的行中
    var_name:字符串 新的列名
    value_name:列的值的名称
    col_level:如果dataframe的列是多级索引，指定要使用的的级别，默认为None，使用所有级别
    ignore_index:是否重置索引
"""
import numpy as np
import  pandas as pd

df = pd. DataFrame({
'Date': ['2021-01-01', '2021-01-02', '2021-01-03'],
'Temperature': [5, 3, 6],
'Humidity': [80, 75, 70],
})
print(df)


"""
         Date     variable  value
0  2021-01-01  Temperature      5
1  2021-01-02  Temperature      3
2  2021-01-03  Temperature      6
3  2021-01-01     Humidity     80
4  2021-01-02     Humidity     75
5  2021-01-03     Humidity     70

"""
print(df.melt( ['Date'], var_name='Metric', value_name='Value'))
print(df.melt(['Date']))