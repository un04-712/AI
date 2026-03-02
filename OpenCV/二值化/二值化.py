# 使用阈值法去二值化一张图像，且图像必须是灰度图

import cv2
import numpy as np

image = cv2.imread('../10000.jpg')
# 使用opencv的cvtColor灰度化图片
cv_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用opencv的接口函数去二值化灰度图
# ret存放的是二值化所用的阈值，如果我们使用阈值法等方法时ret 没有任何作用，
# 当我们使用OTSU去计算阈值最合适的阈值时，ret就有用了
# cv_thresh里存放的是二值化后的图
ret,cv_thresh= cv2.threshold(cv_gray, 127, 255, cv2.THRESH_BINARY)
# # 创建一个与灰度图大小相同的单通道图像，
# image_thresh = np.zeros((cv_gray.shape[0], cv_gray.shape[1]), dtype=np.uint8)
#
# # 定义阈值法需要的阈值
# thresh = 127
# # 定义阈值法需要的最大值
# maxval = 255
#
# for i in range(cv_gray.shape[0]):
#     for j in range(cv_gray.shape[1]):
#         #如果像数值小于阈值，就设置为0，否则设置为maxval
#         if cv_gray[i,j] < thresh:
#             image_thresh[i,j] = 0
#         else:
#             image_thresh[i,j] = maxval
#
# cv2.imshow('image', image)
# cv2.imshow('thresh', image_thresh)
# cv2.waitKey(0)
cv2.imshow('cv_gray', cv_gray)
cv2.imshow("cv_thresh", cv_thresh)
cv2.waitKey(0)