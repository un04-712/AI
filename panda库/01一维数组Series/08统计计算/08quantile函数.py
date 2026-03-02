"""
    分位数:统计学·中用来描述数据集分布的一个概念，他将数据分成若干个等分，帮助我们理解数据在不同范围的分布情况
    分位数q:统计学用来描述数据集的分布的一个概念,它将数据分成若干个等份,帮助我们
理解数据在不同范围里面的分布情况
n:series长度
pandas:分位数对应的位置计算步骤
1.分位数对应的位置;index=q *(n-1)
2.index是一个整数 则直接取该位置上的值 如果不是整数则进行插值计算
i为index整数部分 f为index小数部分
linear:
lower:
higher:
nearest
midpoint

Series.quantile(q=0.5, interpolation='linear')

Q = xi+f*(xi+1-xi)



"""
import pandas as pd
import numpy as np
"""
[1,2,3,4,5] index = 0.3*4 = 1.2 Q= 2+0.2*(3-2)=2.2
"""


s1 = pd.Series([1,2,3,4,5])

q = 0.5

print(s1.quantile(q,interpolation='linear'))