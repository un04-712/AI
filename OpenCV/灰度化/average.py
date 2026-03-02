# 使用平均值的方法去灰度化一张彩色图
import cv2
import numpy as np

img_np = cv2.imread(r'../10000.jpg')

image_shape = img_np.shape

image_gary = np.zeros((image_shape[0],image_shape[1]),dtype=np.uint8)

for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        image_gary[i][j] = ((int(img_np[i,j][0]) + int(img_np[i,j][1])) + int(img_np[i,j][2])) // 3
cv2.imshow('img_np',img_np)
cv2.imshow('image_gary',image_gary)
cv2.waitKey(0)

