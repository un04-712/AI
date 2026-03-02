"""
    用来绘制DataFrame可视化图标
    DataFrame.plot(*args,**kwargs)

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
import pandas as pd
import matplotlib.pyplot as plt
data={
    '编号':[1,2,3],
    '姓名':['小明','小刚','小红'],
    '年龄':[20,21,19],
    '成绩':[78,64,89]
}
df = pd. DataFrame (data)
print(df)
df.plot(kind='bar')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用雅黑字体
plt.rcParams['axes.unicode_minus'] = False


plt.show()

