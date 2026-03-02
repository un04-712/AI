"""
    plt.plot:绘制线
      plot([x], y, [fmt],data=None, **kwargs)
      x：可以是一个列表或者数组，如果x未被指定，默认为range(len(y))
      y：可以是一个列表或者数组
      fmt：定义图形的颜色和样式
      颜色：r:红  g:绿  b:蓝  c:青  m:洋红  k:黑
      标记：.:点  o:圆  s:方形  ^:三角形  d:菱形  x:叉号
      线形：-:实线(默认)  --:虚线  ::点线  -.:点划线
      **kwargs:进一步定义图形的属性
        label:图例的标签
        linewidth:线宽
        color:颜色
        marker:标记样式
        markersize或者ms:标记点大小
        markeredgecolor:标记点边缘颜色
        markeredgeeidth:标记点边缘大小
        markerfacecolor:标记点内部颜色
        alpha:图像透明度

"""
import matplotlib.pyplot as plt
import numpy as np

# #生成sin函数的图像
# x = np.arange(0, 2 * np.pi, 0.1)
# y = np.sin(x)
#
# #绘制线图
# plt.plot(x, y, 'og-.', label='sine wave', linewidth=2, ms=2, alpha=0.5)
# plt.legend()
# #显示图像
# plt.show()
#
# #生成cos函数图像
#
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.cos(x)
#
# #绘制线图
# plt.plot(x, y, 'og-.', label='sine wave', linewidth=2, ms=2, alpha=0.5)
#
# plt.legend()
# #显示图像
# plt.show()

#生成直线图

x = np.arange(0, 10)
y = 2 * x + 2

plt.plot(x, y)
plt.show()
