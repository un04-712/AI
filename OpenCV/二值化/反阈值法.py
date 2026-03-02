# 使用反阈值发去二值化灰度图

import cv2

cv_img = cv2.imread('../10000.jpg')

cv_gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

ret,cv_thresh = cv2.threshold(cv_gray,127,255,cv2.THRESH_BINARY_INV)

cv2.imshow('cv_img', cv_img)
cv2.imshow('cv_gray', cv_gray)
cv2.imshow('cv_thresh', cv_thresh)
cv2.waitKey(0)