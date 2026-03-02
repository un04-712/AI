# 对图片中的目标颜色去进行识别
import cv2
import numpy as np

image = cv2.imread('./img.png')

# HSV空间转换 将RGB颜色空间下的转换成HSV颜色空间下的图像
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3 制作掩膜 为了后续遮挡其他不关心的区域，制作一个掩膜
lowerb = np.array([26,43,46])
upperb = np.array([34,255,255])

# inRange函数的作用，生成一个与原始图像大小相同的单通道图，其值要么是255，要么是0
# 第一个参数：原始图像
# 第二个参数：寻找范围的最小值
# 第三个参数：寻找范围的最大值
mask = cv2.inRange(image_hsv,lowerb,upperb)

# 与运算：将原始图像和原始图像进行位于操作
color_image = cv2.bitwise_and(image,image,mask=mask)

cv2.imshow('color_image',color_image)
cv2.waitKey(0)