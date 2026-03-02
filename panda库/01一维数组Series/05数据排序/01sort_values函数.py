"""
    按照值对series进行排序
    Series_sort_values()
axis :
    ascending:True为升序,False为降序
    inplace:是否在原始series中操作
    kind : 排序算法
    quicksort:速度最快的,性能平均 但不稳定,最坏的情况下性能较差
    mergesort:稳定的排序算法,性能较好,但是空间复杂度高
    heapsort:空间效率较高,但不稳定
    stable:稳定的排序算法,由mergesort和timesort实现
    na_position:决定nan的放置位置,默认为末尾
        first:放到首位
        last:放到末尾
    ignore_index:为True则重置索引
    key:传入函数地址
"""
import pandas as pd
import numpy as np

s = pd.Series([1,4,6,-1,4,5,-5])
print(s.sort_values())

"""
    key参数的使用
"""

s = pd.Series([-1,4,6,1,4,5,-5,np.nan,-32])
print(s.sort_values(key=lambda x:x**2))