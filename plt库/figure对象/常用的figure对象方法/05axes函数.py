"""
    获取一个图形中所有的轴

"""
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.plot([1, 5], [6, 12])

ax1 = fig.add_subplot(122)
ax1.plot([3, 5], [3, -2])

axes = fig.axes

for ax in axes:
    print(ax)  #每一个子图的x和y的相对位置 轴的宽度和高度
plt.show()
