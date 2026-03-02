"""
    add-axes:往任意位置添加子图
    matplotlib.figure.Figure.add_axes(rect,**kwargs)
    rect:   [左边界，底边界，宽度，高度]

"""
import matplotlib.pyplot as plt

fig = plt.figure()

a = fig.add_axes([0.5,0.5,0.5,0.5])

a.plot([0,1],[1,1])

plt.show()