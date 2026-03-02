"""
    figure:用于创建一个新的图形窗口，，或者获取当前活跃的图形窗口
    每个图形窗口可以包含一个或者多个坐标轴，可以在上面绘制数据
    plt.figure(num=None,figsize=None,dpi=None,facecolor=None,edgecolor=None,frameon=True,clear=False,**kwargs)

    num(可选参数):指定图形窗口的编号或者名称
    figsize():图形窗口的大小，以英寸为单位，主要控制图形的物理尺寸

"""
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6),dpi=120,facecolor='g')

plt.plot(  [1,2,3,4], [1,4,9,16])

plt.show()
"""
num参数介绍
"""


plt.figure(num=1)

plt.plot( [1,2,3],[4,5,6])

plt.title('Figure 1')

plt.figure(num=2)

plt.plot( [1,2,3],[4,5,6])

plt.title('Figure 2')

plt.figure(num=1)

plt.plot( [1,2,3], [2,3,4], label ='update plot')
plt. legend()

plt.show()