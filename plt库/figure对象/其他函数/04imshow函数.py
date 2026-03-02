"""
    显示像素点数据 (图片数据)

    x:图像数据
    cmap:颜色映射 通常是virdis
    norm:用于归一化
    aspect:控制图像纵横比
    interpolation:控制图像缩放时的插值位置
    origin；图像原点

"""
import numpy as np
from matplotlib import pyplot as plt

# 1、显示灰度图像

# 10x10 整数范围(0-255)随机数
image_data = np.random.randint(0,256,(10,10))

# 显示图像
plt.imshow(image_data, cmap='gray' )
plt.colorbar()
plt. show()

# 2、显示彩色图像
#10x10 整数范围(0-255)随机数
image_data = np.random.randint(0,256,(10,10,3))
# 显示图像
plt.imshow(image_data)
plt.colorbar()
plt. show()

# 显示插值图像 billnear

image_data = np.random.randint(0,256,(10,10))

plt.imshow(image_data, interpolation='bilinear')
plt.colorbar()
plt. show()

# 显示热图
image_data = np.random.randint(0,256,(100,100))

plt.imshow(image_data, cmap='hot')
plt.colorbar()
plt.show()
