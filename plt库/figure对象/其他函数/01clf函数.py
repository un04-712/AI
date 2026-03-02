"""
    用于清除内容
"""
from matplotlib import pyplot as plt
import numpy as np

# 创建数据
xs = np.arange(0,10,0.01)
y1 = np.sin(xs)

fig, axes = plt.subplots ( 2, 2,figsize=(10,8))

# 第一个子图
axes[0][0].plot(xs, y1)
axes[0][0].set_title('Sine Wave')
axes [0][0]. set_xlabel ('X-axis')
axes[0][0].set_ylabel('y-axis')

fig.subplots_adjust(left=0.2,right=0.8,top=0.8,bottom=0.2,wspace=0.8,hspace=0.8)

# plt.clf()

plt.show()
