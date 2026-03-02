"""
    用于将DataFrame中分割成多个组,并允许对这些分组进行操作,比如计算每个组的总和,平均值,最大值等
    DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True)

    by:确定分组依据,如果by是一个函数,它会在对象索引的每个值上调用,入股传递了字典或series,将使用这些对象的值来确定组。如果传递了
    长度等于所选轴的列表或ndarray,则直接使用这些值来确定组
    axis:沿着哪个轴去处理
    level:用于指定分组所依据的级别
    as_index:是否将分组键作为结果的索引 ，为True的话，分组名称将作为结果的索引，如果为false,则结果会保持原有的DataFrame结构
    sort:是否对结果进行排序
    group_keys:是否包含分组键
    observed:是否仅包含实际观察到的分类值
    dropna:是否从结果中排除包含nan的组
"""
#单级索引
import pandas as pd
import  numpy as np

df = pd.DataFrame(
    {
        'A':['foo','bar','foo','bar','foo','bar', 'foo', 'foo'],
        'B': ['one' , 'one' , 'two' , 'three' , 'two' , 'two' , 'one' , 'three' ],
        'C':[1,3,2,5,4,1,2,3],
        'D':[2,5,3,7,6,2,4,6]
    }
)
grouped = df.groupby(['A' , 'B'])
print(df)
# print(list(grouped))

print(grouped.mean())

# 多级索引
import pandas as pd
# 创建两个列表,它们将用作多级索引的级别
arrays = [['Falcon', 'Falcon','Parrot', 'Parrot'], # 第一级索引的值
         ['Captive','Wild','Captive','Wild']] # 第二级索引的值
# 使用arrays列表创建一个DataFrame,'Max Speed'列包含对应于多级索引的数据
df = pd.DataFrame({'Max Speed':[390., 350.,30., 20.]},index=arrays)#使用arrays列表作为多级索引
# 打印原始DataFrame,以查看其结构和数据
print(df)
# 使用groupby方法按第一级索引(即’arrays'列表的第一个元素)分组
# level=0表示按照多级索引的第一级进行分组
res =df.groupby(level=0).mean()#计算每个组(即每个不同的第一级索引值)的平均速度
# # 打印分组后的平均值,显示每个动物的Max Speed的平均值
print(res)
