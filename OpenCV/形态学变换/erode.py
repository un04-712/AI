import cv2

image = cv2.imread('./img.png')

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, image_thresh = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY)

# 进行腐蚀操作
# 构建腐蚀操作所需要用到的核
# cv2.getStructuringElement 用来生成形态学变换的核
# 第一个参数：指定核的形状
# 第二个参数：指定核的大小，以元组的形式传递
# 第三个参数：指定十字形状的核值分布
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

# 进行滑动计算
# erode:用来对二值化图像进行腐蚀操作，必须要准备参数
# 要进行腐蚀的二值化图像
# 用来滑动计算的结构化元素
image_erode = cv2.erode(image_thresh,kernel)

# 显示图像
cv2.imshow('erode', image_erode)
cv2.waitKey(0)