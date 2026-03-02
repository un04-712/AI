"""
    数据透视表:是一种用于数据分析的工具，它通过对原始数据进行汇总、分类、重组和聚合，帮助我们从不同角度快速总结、分析、和可视化数据，
    数据透视表在处理大量复杂数据是非常有用，可以帮助我们更容易发现数据中的模式、趋势、关系
    DataFrame.pivot_table()
    values:要聚合和列名或列名列表,如果未指定,则使用所有数据
    index:作为新dataframe的行索引的列名和列名列表
    columns:作为新dataframe的列标签的列名或列名列表
    aggfunc:聚合函数
        单个函数
        函数列表
        字典:键是列名 值是聚合函数
    fill_value:用于填充缺失值
    margins:是否添加总计行和总计列
    dropna:是否删除缺失值所在的行
    margins_name:总计行和总计列的名称
    observed:是否仅显示已观察到的列别
    sort:是否对结果进行排序
"""


import pandas as pd
# 示例数据:包含产品、地区、销重和销售额
df = pd.DataFrame({
    'Date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02', '2021-01-03', '2021-01-03' ],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Product': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 250, 300, 350],
    'Revenue': [1000, 1500, 2000, 2500, 3000, 3500]
}
)

print(df)

df_pivot_table = df.pivot_table(
    index = ['Region', 'Product' ],
    values =['Sales' , 'Revenue' ],
    aggfunc={'Sales':'mean','Revenue' : 'sum'},
    fill_value = 0
)
print(df_pivot_table)



