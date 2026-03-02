# 对二值化操作进行膨胀操作

import cv2
# 读取彩色图
image = cv2.imread("./img.png")
# 转化为灰度图
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 转化为二值化图
ret,image_thresh = cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY)

# cv2.getStructuringElement 用来生成形态学变换的核
# 第一个参数：指定核的形状
# 第二个参数：指定核的大小，以元组的形式传递
# 第三个参数：指定十字形状的核值分布
# 构建核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# dilate:用来对二值化图像进行膨胀操作，必须要准备参数
# 要进行膨胀的二值化图像
# 用来滑动计算的结构化元素
image_dilate = cv2.dilate(image_thresh,kernel)

cv2.imshow('image_dilate',image_dilate)

cv2.waitKey(0)
