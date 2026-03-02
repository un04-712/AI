import cv2
import numpy as np

image = cv2.imread("./img.png")

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('image_hsv', image_hsv)
cv2.waitKey(0)
# 制作掩膜
lowerb = np.array([100, 43, 46])
upperb = np.array([124, 255, 255])

mask = cv2.inRange(image_hsv, lowerb, upperb)
cv2.imshow('mask', mask)
cv2.waitKey(0)
# 开运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# 图片颜色替换
# for i in range(mask_open.shape[0]):
#     for j in range(mask_open.shape[1]):
#         if mask_open[i,j] == 255:
#             image_hsv[i,j] = [255, 0, 0]
image_hsv[mask_open == 255] = (255, 0, 0)

cv2.imshow("image_hsv", image_hsv)
cv2.waitKey(0)
