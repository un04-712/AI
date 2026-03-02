"""
    xlabel:设置x轴的标签
    xlabel:设置y轴的标签
    title:设置图的标题(显示在图顶部的文本)
    subplot:用于在一个图形窗口创建多个子图布局
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('T')
plt.ylabel('y')
plt.title('sin')
plt.show()



"""
    subplot:
    
    plt.subplot(nrows,ncols,plot_number)
    nrows:子图的行数
    ncols:子图的列数
    plot_number：当前子图的标号，从1开始
"""
x = np.arange(0,3*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

#创建一个两行一列的子图，操作第一个子图
plt.subplot(2,1,1)
plt.plot(x,y_sin)


plt.xlabel('T')
plt.ylabel('y')
plt.title('sin')


plt.subplot(2,1,2)
plt.plot(x,y_cos)


plt.xlabel('T')
plt.ylabel('y')
plt.title('cos')

plt.show()