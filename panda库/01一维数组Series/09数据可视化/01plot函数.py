"""
    用来绘制Seriesde1可视化图标
    Series.plot(*args,**kwargs)

    kind:
            'line'  'bar'
            'barh'  水平柱状图
            'hist'  直方图
            'box'       箱线图
            'kde'       核密度估计图
            'area'      面积图
            'pie'       饼图
            'scatter'   散点图
            'hexbin'   六边形箱图
    figsize:图标的尺寸
    use_index:是否使用Series的索引来作为x轴的标签，默认为True
    title:标题
    grid:是否显示网格线
    legend:是否显示图例
    xtickets:x轴的刻度位置
    ytickets:y轴的刻度位置
    xlim:x轴的范围
    ylim:y轴的范围
    color:绘制颜色
    label:图例的标签
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series(np.random.rand(20))

s.plot(kind='pie',title='random fig',legend=True)

plt.show()