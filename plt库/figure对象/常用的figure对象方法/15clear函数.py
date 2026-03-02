"""
    如果作用与axes 清除子图内容

    如果作用与figure  清除图形窗口的内容

"""

from matplotlib import pyplot as plt
import numpy as np

# 创建数据
x = np.arange(0,10,0.01)
y = np.sin(x)

fig, axes = plt. subplots ( 2,  2, figsize=(10,8))

#第一个子图
axes[0][0].plot(x,y)
axes [0] [0].set_title('Sine Wave' )
axes[0] [0].set_xlabel ('X-axis')
axes[0][0].set_ylabel('y-axis')

fig.subplots_adjust(left=0.2,right=0.8,top=0.8,bottom=0.2,wspace=0.8,hspace=0.8)

# axes[0] [0]. clear()
fig.clear()

plt. show()