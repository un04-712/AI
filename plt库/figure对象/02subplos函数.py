"""
    subplots:创建多个子图
    fig,axes = subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, width_ratios=None, height_ratios=None, subplot_kw=None, gridspec_kw=None, **fig_kw)

    arows:子图的行数
    ncols:子图的列数
    sharex:布尔值，是否共享x坐标
    sharey:布尔值，是否共享y坐标
    squeeze:布尔值，如果为true，如果只创建一个子图，返回一个子图对象而不是一个只包含一个子图对象的数组
    width_ratios:
    height_ratios:
    subplot_kw:字典值，表示额外的关键字传递给add_subplot调用，可以用来设置子图的属性
    gridspec_kw:字典值，以用来设置子图布局窗口属性

    返回值：
    fig:图形窗口对象
    axes:子图对象，数组类型
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.01)
y = np.sin(x)
z = np.cos(x)
m = np.tan(x)
n = 1 / (1 + np.exp(-x))

#创建一个两行一列的子图，操作第一个子图
plt.subplot(2, 2, 1)

plt.plot(x, y)

plt.subplot(2, 2, 2)

plt.plot(x, z)

plt.subplot(2, 2, 3)

plt.plot(x, m)
plt.subplot(2, 2, 4)

plt.plot(x, n)
plt.show()

"""
    subplot实现
"""
#创建两行两列的子图，返回图形窗口对象和子图对象数组
fig, axes = plt.subplots(2, 2, figsize=(10, 8), width_ratios=[1, 2], height_ratios=None)

#第一个子图
axes[0][0].plot(x, y)
axes[0][0].set_title('sine wave')
axes[0][0].set_xlabel('x')
axes[0][0].set_ylabel('y')

axes[0][1].plot(x, z)
axes[0][1].set_title('cose wave')
axes[0][1].set_xlabel('cos-x')
axes[0][1].set_ylabel('cos-y')

axes[1][0].plot(x, m)
axes[1][0].set_title('tan wave')
axes[1][0].set_xlabel('tan-x')
axes[1][0].set_ylabel('tan-y')

axes[1][1].plot(x, n)
axes[1][1].set_title('sig wave')
axes[1][1].set_xlabel('sig-x')
axes[1][1].set_ylabel('sig-y')

fig.suptitle('text-name')
fig.tight_layout()
plt.show()


"""
    subplot_kw和gridspec_kw
    subplot_kw:
            xlim和ylim:x轴和y轴的显示范围
            xlabel和ylabel标签:x轴和y轴的标签
            title:子图的标题
            facecolor和edgecolor
            
"""

fig, axes = plt.subplots(2, 2, )

#第一个子图
axes[0][0].plot(x, y)
axes[0][0].set_title('sine wave')
axes[0][0].set_xlabel('x')
axes[0][0].set_ylabel('y')

axes[0][1].plot(x, z)
axes[0][1].set_title('cose wave')
axes[0][1].set_xlabel('cos-x')
axes[0][1].set_ylabel('cos-y')

axes[1][0].plot(x, m)
axes[1][0].set_title('tan wave')
axes[1][0].set_xlabel('tan-x')
axes[1][0].set_ylabel('tan-y')

axes[1][1].plot(x, n)
axes[1][1].set_title('sig wave')
axes[1][1].set_xlabel('sig-x')
axes[1][1].set_ylabel('sig-y')

fig.suptitle('text-name')
fig.tight_layout()
plt.show()
