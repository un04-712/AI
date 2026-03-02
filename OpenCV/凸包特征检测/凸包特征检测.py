#导库
import cv2

#读取图像
image = cv2.imread("../10000.jpg")
#灰度化
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#二值化
ret,image_thresh = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY)
#寻找轮廓
contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#查找凸包，获取凸包点
cot = contours[0]
hull = cv2.convexHull(cot)
#绘制凸包
image_poly = cv2.polylines(image, [hull], True, (0, 255, 255))

cv2.imshow('image', image)
cv2.imshow('image_poly', image_poly)
cv2.waitKey(0)
