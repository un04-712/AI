import cv2

image = cv2.imread('../10000.jpg')

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 对转化好的灰度图进行自适应二值化
# cv2.adaptiveThresh:用来对单通道进行自适应二值化
# 第一个参数:单通道图
# 第二个参数:二值化过程中所用到的最大值
# 第三个参数:计算阈值的方法  平均值法：cv2.ADAPTIVE_THRESH_MEAN_C 高斯加权均值法：cv2.ADAPTIVE_THRESH_GAUSSIAN_C
# 第四个参数:二值化的方法
# 第五个参数:blocksize大小，通常为奇数
# 第六个参数:要减去常数c的大小file:///C:/Users/86132/xwechat_files/wxid_jgyfefu408kx22_684c/temp/RWTemp/2025-08/02fa27a254f50336a8a7ba1c5a9833e5/b1aa01e5dd6cd57220b733f03f0b9403.jpg
image_adathresh = cv2.adaptiveThreshold(image_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,10)


# 对计算的结果进行显示
cv2.imshow('image',image)
cv2.imshow('image_gray',image_gray)
cv2.imshow('image_adathresh',image_adathresh)
cv2.waitKey(0)
