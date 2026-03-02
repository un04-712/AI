import cv2
import numpy as np


# 做一个函数用来统计和绘制直方图
def calcDraw(image_gray):
    # calcHist:参数都是数组
    # 绘制直方图
    image_cal = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    # 为了归一化的操作，找到image_cal里面的最大值
    minval,maxval,minloc,maxloc = cv2.minMaxLoc(image_cal)
    # 创建一个256*256的模板图
    histImg = np.zeros((256,256,3), np.uint8)
    for h in range(256):
        # 归一化处理，在循环里，对每一列数据，进行归一化处理，防止其超出模板的图范围
        intensity = int(256*image_cal[h] / maxval)
        cv2.line(histImg,(h,256),(h,256 - intensity),(0,0,255),2)
    return histImg


image = cv2.imread("../10000.jpg")

# 灰度化
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 绘制直方图
image_hist = calcDraw(image_gray)

# 标准的直方图均衡化
# image_equal = cv2.equalizeHist(image_gray)
# image_equalHist = calcDraw(image_equal)
# 自适应直方图均衡化
clahe = cv2.createCLAHE(2,(8,8))
image_clahe = clahe.apply(image_gray)
image_clahe1 = calcDraw(image_clahe)


cv2.imshow('image',image)
cv2.imshow("image_hist",image_hist)
# cv2.imshow("image_equalHist",image_equalHist)
cv2.imshow("image_clahe",image_clahe)
cv2.imshow("image_clahe1",image_clahe1)
cv2.waitKey(0)