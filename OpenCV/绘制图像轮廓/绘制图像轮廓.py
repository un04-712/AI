import cv2

image = cv2.imread("../10000.jpg")
#复制一份原始图像来绘制轮廓


# 灰度化图像
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 二值化图像
ret,image_thresh = cv2.threshold(image_gray, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)


# 查找轮廓
# contours:存储了所有的轮廓点对应的坐标，比如说contours[0]就存储了第0个轮廓的点的坐标，contours[1]就存储了第一个轮廓的点的坐标
# hierarchy:存储了对应轮廓的层级关系，hierarchy[0]就存储了第0个轮廓的层级关系
contours,hierarchy = cv2.findContours(image_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(image,contours,1,(0,0,255),thickness=cv2.FILLED)

cv2.imshow("image",image)
cv2.waitKey(0)