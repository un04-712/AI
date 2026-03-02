"""
    按照索引顺序进行排序
    Series.sort_index()

    level:如果索引是多级索引(也称为层次化索引或MultiIndex),则可以指定先要排序的级别
    ascending:True为升序，False为降序
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
    sort.remaining:如果为True,在level排序完成之后，会在排序基础上对剩下级别元素进行排序

"""
import pandas as pd
import numpy as np
"""
    基本使用方法
"""

s = pd.Series([10,11,12,13,14,15,16,np.nan, 43], index=[1,2,4,3,9,np.nan, 5,23,56])

print(s.sort_index())


"""
    多级索引
"""


import pandas as pd
import numpy as np
arrays = [np.array(['qux', 'qux', 'foo', 'foo',
                    'baz', 'baz', 'bar', 'bar']),
          np.array(['two', 'one', 'two', 'one',
                    'two', 'one', 'two', 'one'])]

s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=arrays)

print(s)

res = s.sort_index(level=1, sort_remaining=False)
print(res)
