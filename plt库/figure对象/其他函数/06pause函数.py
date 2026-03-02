"""
    用于动画或交互式绘画过程中暂停一段时间，这个函数在动画制作或者需要绘图之前插入延迟时非常有用
    matplotlib.pyplot.pause(interval)

    interval:暂停的秒数
    更新显示:   可以不借助plt.show能直接显示出来
"""
import matplotlib.pyplot as plt
import numpy as np
plt.figure()
plt.plot([1,2,3],[4,5,6])

plt.pause(2)

fig,ax = plt.subplots()

t = np.arange(0,10,0.1)
s = np.sin(t)

ax.plot(t,s)

for i in np.arange(0,100*np.pi,0.02):
    t = np.arange(0, 10, 0.1) + i
    s = np.sin(t)
    ax.plot(t,s)
    fig.clear()
    plt.pause(0.2)