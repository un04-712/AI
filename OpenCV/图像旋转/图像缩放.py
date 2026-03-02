import cv2

image = cv2.imread("../10000.jpg")

# 图片缩放
# dsize和fx，fy不能同时使用，如果同时使用，会以dsize的标准进行缩放
# 如果想要使用resize函数，就必须两个参数：src和dsize
# 如果不想使用dsize赋值位None就可以了
image_resize = cv2.resize(image,None,fx=3,fy=3,interpolation=cv2.INTER_LINEAR)

cv2.imshow('image_resize',image_resize)
cv2.waitKey(0)