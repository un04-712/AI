"""
    为子图提供更灵活的布局，在matplotlib中，默认的子图布局是通过plt.subplot或者
    跑plt.subplots等函数实现，但这些函数都是按照行列均匀划分子图，而GridSpec
    可以根据具体需求定制子图的位置和大小

"""
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

"""
    基本用法
"""

fig = plt.figure()

#创建4个网格
gs = GridSpec(2,2)

a1 = fig.add_subplot(gs[0,0])
a2 = fig.add_subplot(gs[0,1])
a3 = fig.add_subplot(gs[1,0])
a4 = fig.add_subplot(gs[1,1])

plt.show()


fig = plt.figure()

gs = GridSpec(3,3)
a5 = fig.add_subplot(gs[0,0])
a6 = fig.add_subplot(gs[0,1])
a7 = fig.add_subplot(gs[1:3,0])
a8 = fig.add_subplot(gs[1,1:3])

plt.show()


