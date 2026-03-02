"""
    plt.pie
    pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, *, normalize=True, hatch=None, data=None)
    x:饼图中每个扇形的尺寸，为非负数组或序列
    explode:一个与x相同长度的数组，用于指定每个扇形是否突出显示，如果explode[i]!=0,则会与其他扇形分离
    colors:颜色列表，用于指定每个扇形的颜色
    autopct:格式化字符串，用来显示每个扇形的字符串,使用%.1f%%来表示一位小数的百分比
    startangle:饼图开始的角度
    radius:饼图的半径
    wedgeprops:字典数据，用于指定每个扇形的属性，如边缘颜色或宽度
    textprops:字典数据 用于指定饼图中标签的文本属性
    center:一个元组，用于指定饼图的中心位置
    frame:布尔值，用于指定是否为饼图添加一个坐标轴
    rotatelabels:是否指定旋转标签以适应扇形
    normalize:布尔值,如果为True,则x中的值将被归一化，以使得他的总和为1
    hatch:进行图案补充    *+-./OX\ox|
"""
import matplotlib.pyplot as plt
import numpy as np

size = [17.3, 18.0, 19.5, 16.5, 13.5, 15]
labels = ['鸡腿饭', '麻辣烫', '冒菜', '鸡架拌饭', '汉堡', '牛肉面']
color = ['#42B027', '#C2A01B', '#195B9C', '#784315', '#804EAD', '#EB0E31']
# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号
plt.pie(size, colors=color,
        labels=labels,
        autopct='%.1f%%',
        textprops=dict(color='white')
        )
plt.legend()
plt.show()
