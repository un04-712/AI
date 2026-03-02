"""
    绘制数据直方图
    Series.hist(by=None, ax=None, grid=True, xlabelsize=None,xrot=None,
    ylabelsize=None, yrot=None, figsize=None, bins=10,backend=None,
    legend=False **kwargs)

    by:非none则表示将数据分组并分布绘制每个组的直方图
    grid:显示网格图
    xlabelsize:x轴标签字体旋转大小
    xrot:设置x轴标签的旋转角度
    ylabelsize:y轴标签字体旋转大小
    yrot:设置x轴标签的旋转角度
    figsize:图标大小
    bins:柱子数量或具体的边界
    legend:是否显示图例

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series(np.random.rand(1000))

s.hist(bins=40,legend=True)

plt.show()
