import cv2

image = cv2.imread("../10000.jpg")

# 使用cv2.flip: 对图像进行翻转
# 第一个参数：要翻转的原始图像
# 第二个参数：标志位，0：表示绕x轴进行上下翻转，>0：表示绕y轴进行左右翻转，<0：表示绕x轴和y轴个进行一次翻转
image_flip = cv2.flip(image, -1)

cv2.imshow('image', image)
cv2.imshow('image_flip', image_flip)
cv2.waitKey(0)
