import cv2
import numpy as np

image = cv2.imread("../10000.jpg")



image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, image_thresh = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite("../10000_gray.png", image_thresh)

cv2.imshow('image_thresh', image_thresh)
cv2.waitKey(0)


# image_shape = image.shape
# image_thresh = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)
# min_value = np.min(image_gray)
# max_value = np.max(image_gray)
# print(min_value, max_value)
# # 前景像素点
# n_0 = 0
# # 背景像素点
# n_1 = 0
# # 前景像素点占比
# w_0 = 0
# # 背景像素点占比
# w_1 = 0
# # 前景平均像素值
# u_0 = 0
# # 背景平均像素值
# u_1 = 0
# # 全局平均像素值
# u = 0
#
# rows = image_shape[0]
# cols = image_shape[1]
# # 定义一个字典来存储每一个阈值对应的最大类间方差
# dict = {}
#
# for t in range(min_value , max_value, 1):
#     # 定于列表来存储我们的前景点和背景点
#     foreground = []
#
#     background = []
#     # 定义一个变量来存储前景像数值的总数
#     forefix = 0
#     # 定义一个变量来存储背景像数值的总数
#     backfix = 0
#     # 定义变量用来存储所有像素点的总像素值
#     pix = 0
#     for i in range(image_shape[0]):
#         for j in range(image_shape[1]):
#             if image_gray[i, j] > t:
#                 foreground.append(image_gray[i, j])
#                 # 前景像素点的总值
#                 forefix += image_gray[i, j]
#
#                 pix += image_gray[i, j]
#             else:
#                 background.append(image_gray[i, j])
#                 # 后景像素点的总值
#                 backfix += image_gray[i, j]
#
#                 pix += image_gray[i, j]
#     n_0 = len(foreground)
#     print(n_0)
#
#     n_1 = len(background)
#     print(n_1)
#     w_0 = n_0 / (rows * cols)
#     w_1 = n_1 / (rows * cols)
#     u_0 = forefix / n_0
#     u_1 = backfix / n_1
#     u = pix / (rows * cols)
#
#     #通过最大类间方差计算最后的结果
#     g = w_0 * ((u_0 - u) ** 2) + w_1 * ((u_1 - u) ** 2)
#     # 将获取到的最大类间方差值和对应的阈值存储到字典里
#     dict[t] = g
# # for循环结束后寻找最大类间方差
# thresh = max(dict, key=dict.get)
# maxval = 255
# for i in range(image_shape[0]):
#     for j in range(image_shape[1]):
#         #如果像数值小于阈值，就设置为0，否则设置为maxval
#         if image_gray[i, j] < thresh:
#             image_thresh[i, j] = 0
#         else:
#             image_thresh[i, j] = maxval
#
# cv2.imshow("thresh", image_thresh)
# cv2.waitKey(0)
