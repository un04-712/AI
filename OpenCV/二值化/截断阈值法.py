# 使用截断阈值法来二值化灰度图
import cv2
import numpy as np

cv_image = cv2.imread("../10000.jpg")

cv_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

thresh = 127
maxval = 200

# cv_shape = cv_gray.shape

# cv_thresh = np.zeros((cv_shape[0],cv_shape[1]),dtype=np.uint8)

# for i in range(cv_shape[0]):
#     for j in range(cv_shape[1]):
#         if cv_gray[i,j]>thresh:
#             cv_thresh[i,j]=thresh
#         else:
#             cv_thresh[i,j]=cv_gray[i,j]
#
# cv2.imshow('cv_thresh', cv_thresh)
# cv2.waitKey(0)
ret, cv_thresh = cv2.threshold(cv_gray, thresh,maxval, cv2.THRESH_TRUNC)

cv2.imshow('cv_image', cv_image)

cv2.imshow('cv_gray', cv_gray)

cv2.imshow('cv_thresh', cv_thresh)

cv2.waitKey(0)
