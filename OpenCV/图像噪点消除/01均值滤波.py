import cv2

image = cv2.imread("../10000.jpg")

# 获取卷积核(滤波器)并进行均值滤波操作
image_blur = cv2.blur(image,(3,3))

cv2.imshow("image",image)
cv2.imshow("image_blur",image_blur)
cv2.waitKey(0)