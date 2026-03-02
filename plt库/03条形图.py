"""
    plt.bar
    bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
    x:x的坐标，这个参数可以是单个值也可以是一个数组，可以是字符
    height:条形图的高度，这个参数可以是单个值也可以是一个数组
    width:条形的宽度，参数可以是单个值，也可以是一个数组
    bottom:条形的起始位置，默认为0，可以是单个值也可以是一个数组
    align:条形的对齐方式center(中心对齐),edge(左对齐)
    kwargs:
        facecolor 和 edgecolor
        linewidth:条形边缘的宽度
        linestyle:条形边缘的线型  -- 虚线  :点线  -.: 点划线
        alpha
        hatch:条形的填充图案 o:圆圈  x:叉号
        log:如果设置为True,条形的高度以对数尺度表示
        Label:图例标签
        picker 控制条形是否可以被交互选择
"""
import matplotlib.pyplot as plt
import numpy as np

# x = np.array(['A','B','C','D','E'])
# y = np.array([16,28,37,69,85])
#
# plt.bar(x,y,width=0.5,bottom=5,align='center',label='score')
#
# plt.legend()
# plt.show()

"""
    picker参数使用
"""
# x = np.array(['A','B','C','D','E'])
# y = np.array([16,20,33,60,77])
# plt.bar(x,y,picker=True)
#
# def on_pick(event):
#     if isinstance(event.artist,plt.Rectangle):
#         event.artist.set_facecolor('red')
#         plt.draw()
# plt.gcf().canvas.mpl_connect('pick_event',on_pick)
# plt.show()

import matplotlib.pyplot as plt
import mplcursors

# 数据
names = ["xiaozhang", "xiaoli", "xiaowang", "xiaozhao", "xiaosun", "xiaoqian", "xiaowu", "xiaozheng", "xiaofen", "xiaoma"]
scores = [55, 80, 75, 90, 82, 30, 42, 99, 54, 66]

# 绘制条形图
plt.figure(figsize=(10, 6))
plt.bar(names, scores, color='blue',linewidth=2,edgecolor='green',hatch='*',linestyle=':')
plt.xlabel('name')
plt.ylabel('score')
plt.title('zuoye')
# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号


plt.tight_layout()
plt.show()