"""
    plt.scatter
    scatter(x,y,s=None，c=None,marker=None,cmap=None)
    s:散点的大小，可以是标量或数组，用于指定每个点的大小
    c:散点的颜色，可以是单个颜色，也可以是数组，为每个点指定颜色，如果提供了cmap参数，则c可以是颜色的映射值
    cmap:用于将c的数值映射到颜色
        viridis:默认渐变 从暗紫色到亮黄色
        plasma:从暗紫色到亮红色
        inferno:从黑色到亮黄色
        cividis:色盲友好的渐变
        coolwarm:蓝红色的渐变，用于适用温度等数据的可视化
    marker：.:点  o:圆  s:方形  ^:三角形  d:菱形
    norm:用于标准化c的颜色的normalize对象，确保数据在指定范围内的颜色映射
        none:会根据c参数中传递的数值，自动计算出最大值和最小值，并将这些颜色映射到0-1的范围内
        normalize:线性映射
        LogNorm:对数映射
        TwoSlopeNorm:斜率中点映射
    vmin,vmax(可选) 分别是c中数据的最大值和最小值
    alpha:透明度
    linewidths:散点边缘的线框
    edgecolors:
"""
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.pyplot import yscale
# from numpy.random import normal
#
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
#
# plt.scatter(x, y, s=5, c=y, cmap='coolwarm', marker='.', linewidths=3, edgecolors='c')
#
# plt.colorbar()
# plt.show()
#
# #将一组均值为0，标准差为3的一组随机数绘制到散点图中。样本个数50个
# y = np.random.normal(0, 3, 50)
#
# x = np.arange(50)
#
# plt.scatter(x, y, s=5, c=y)
#
# plt.show()
#
# # 数据
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 数据
# x = np.array(
#     [67.66397446, 87.8932002, 15.49173638, 49.00073811, 93.34772669, 29.19484048, 64.30818057, 88.35988062, 47.16284695,
#      47.83597447])
# y = np.array([16.267041703293813, 22.026598231507805, 4.595525565959681, 11.77011884672302, 23.328619677331318,
#               6.879516204429002, 15.71628337101803, 21.571674589732197, 12.279129102861052, 11.306641112119534])
#
# # 绘制散点图
# plt.figure(figsize=(10, 6))
# plt.scatter(x, y, color='blue')
#
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('scatter')
#
# plt.show()

import numpy as np
from matplotlib import pyplot as plt

y = np.random.randn(100)
x = np.linspace(0,10,100)

plt.scatter(x,y,marker='^',c='#8A35CF',s=100,alpha=0.5,linewidths=10,edgecolors='#FF41BD')

plt.show()