"""
    inplace=False, kind='quicksort', na_position='last'
    ignore_index=False,key=None)
    by: 排序的列名或列名列表
    axis : 0 index 1 columns
    ascending:True为升序,False为降序
    inplace:是否在原始dataframe中操作
    kind : 排序算法
        quicksort:速度最快的,性能平均 但不稳定,最坏的情况下性能较差
        mergesort:稳定的排序算法,性能较好,但是空间复杂度高
        heapsort:空间效率较高,但不稳定
        stable:稳定的排序算法,由mergesort和timesort实现
    na_position: 决定NaN值的放置位置 first放在首位 last放在尾部
    ignore_index: 为True则重置索引
如果指定,则这个函数将在排序之前应用于每个值,并且排序将基于这些函数返回的值。

key:传入函数地址


"""

import numpy as np
import pandas as pd
df = pd. DataFrame (
    {
        'col1' : ['a','b','c', np.nan,'d','c'],
        'col2': [2,1,4,8,7,9],
        'col3': [0,1,9,4,2,3],
        'col4' : ['a','b','c','d','e','f'],
    }
)

print(df)

# 对单列进行排序
df = df.sort_values(by=['col1'],kind='stable')
print(df)

# 对多列进行排序
print(df.sort_values(by=['col1','col2'],kind='stable'))