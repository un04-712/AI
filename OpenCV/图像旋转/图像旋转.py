import cv2

image = cv2.imread("../10000.jpg")
angle = 0
scale = 0.5
image_shape = image.shape
# 旋转90°
# image_rotat = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow("image", image)
# cv2.imshow("image_rotat", image_rotat)
# cv2.waitKey(0)
# 构建旋转矩阵
# cv2.getRotationMatrix2D:构建一个2*3的矩阵，包含图像的旋转，平移，缩放
# 第一个参数：旋转中心
# 第一个参数：旋转角度
# 第一个参数：旋转比例
M = cv2.getRotationMatrix2D((image_shape[1] / 2, image_shape[0] / 2), angle, scale)

# 进行图像旋转
# cv2.warpAffine:对图像进行旋转
# 第一个参数：要旋转的图像
# 第二个参数：通过v2.getRotationMatrix2D 获取到的旋转矩阵
# 第三个参数：输出图像的大小
image_rot = cv2.warpAffine(image,M,(image_shape[1],image_shape[0]),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_WRAP)

cv2.imshow("image", image)
cv2.imshow("image_rot", image_rot)
cv2.waitKey(0)