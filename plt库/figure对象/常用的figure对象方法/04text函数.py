"""
    往任意位置添加文本
        matplotlib.axes.Axes.text(x,y,s,**kwargs)

        x,y:文本位置坐标
        **kwargs
"""

import matplotlib.pyplot as plt

fig = plt.figure()

a1 = fig.add_subplot(1, 2, 1)
a1.plot([1, 5], [6, 12])

a2 = fig.add_subplot(1, 2, 2)
a2.plot([-3, 1], [4, -2])

a2.text(0, 0, 'TEST')

fig.suptitle('Line Polt', fontsize=25, color='red')

plt.show()
