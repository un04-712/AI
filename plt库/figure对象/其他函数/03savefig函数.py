"""
    用于将当前文件图形保存到文件中
    用于将当前图形保存到文件中
    matplotlib.pyplot.savefig(fname, dpi='figure', format=None,
    metadata=None, bbox_inches =None, pad_inches=0.1, facecolor='auto',
    edgecolor='auto', backend=None, ** kwargs)

    fname:文件名       figure:使用图形窗口分辨率
    dpi : 分辨率       None:使用的是文件名后缀的文件格式
    format: 文件格式
    metadata:元数据
    bbox_inches:tight:则matplotlib会尝试裁剪图形周围的空白
    pad_inches:填充空白
    facecolor:背景颜色
    edgecolor:边缘颜色
    backend:   用于保存图像的特定后端，通常不需要设置
    kwargs:其他关键字函数

"""


"""
    基本使用
"""

import matplotlib.pyplot as plt
import numpy as np


# 创建数据
xs = np.arange(0,10,0.01)
y1 = np.sin(xs)
y2 = np.cos(xs)
y3 = np.tan(xs)
y4=1/(1+np.exp(-xs))

fig, axes = plt.subplots(  2,  2,figsize=(10,8))
# 第一个子图
axes[0][0].plot(xs, y1)
# 第二个子图
axes[0] [1].plot(xs, y2)
# 第三个子图
axes[1][0].plot (xs, y3)
# 第四个子图
axes[1] [1].plot(xs, y4)

fig.tight_layout()

plt.savefig( 'plot.png', facecolor='r')
plt.show()
"""
metadata
"""
metadata={
    'Title': 'Plot Line',
    'Author': 'John'
}
plt.savefig( 'plot.png',facecolor='#3D9BE8', metadata=metadata)
plt. show()