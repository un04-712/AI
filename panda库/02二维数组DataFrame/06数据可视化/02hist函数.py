"""
    绘制数据直方图
    DataFrame.hist(by=None, axis=None, grid=True, xlabelsize=None,xrot=None,
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
from pandas import DataFrame

data={
    '编号':[1,2,3],
    '姓名':['小明','小刚','小红'],
    '年龄':[20,21,19],
    '成绩':[78,64,89]
}
df = pd. DataFrame (data)
print(df)

help(DataFrame.hist)