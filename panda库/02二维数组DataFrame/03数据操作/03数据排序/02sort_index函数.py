"""
    按照索引顺序进行排序
    DataFrame.sort_index()


    axis:0 index  1 columns
    level:如果索引是多级索引(也称为层次化索引或MultiIndex),则可以指定先要排序的级别
    ascending:True为升序，False为降序
    inplace:是否在原始DataFrame中操作
    kind : 排序算法
        quicksort:速度最快的,性能平均 但不稳定,最坏的情况下性能较差
        mergesort:稳定的排序算法,性能较好,但是空间复杂度高
        heapsort:空间效率较高,但不稳定
        stable:稳定的排序算法,由mergesort和timesort实现
    na_position:决定nan的放置位置,默认为末尾
        first:放到首位
        last:放到末尾
    ignore_index:为True则重置索引
    sort.remaining:如果为True,在level排序完成之后，会在排序基础上对剩下级别元素进行排序


"""
import pandas as pd
import  numpy as np
arrays = [np.array(['qux', 'qux', 'foo', 'foo']),
          np.array(['two', 'one', 'two', 'one'])]

df = pd.DataFrame({'A':[1,2,3,4],'B':[4,3,2,1]},index=arrays)
print(df)

print(df.sort_index(level=0))