# 使用加权平均的方法灰度化一张彩色图

# 如何使用opencv读取一张图片，在opencv里使用cv2.imread读取

# cv2.imread():两个参数，第一个是要读取的图片的位值，第二个参数是要读取文件的格式，默认使用BGR彩色图的格式(读取类型为np数据格式)
# 函数 imread 从指定文件加载图像并返回它。如果无法读取图像（由于缺少文件、权限不当、格式不受支持或无效），则该函数将返回一个空矩阵（ Mat：:d ata==NULL ）
# opencv读取图像格式默认使用BGR的格式存储
import cv2
import numpy as np

image_np = cv2.imread(r"../10000.jpg")

# 使用opencv的接口去灰度化一张彩色图
cv_gray = cv2.cvtColor(image_np,cv2.COLOR_BGR2GRAY)
# shape:是ndarray的一个属性，，用来查看数组的形状
# shape读取到的形状与图像实际宽和高是相反的，shape[0]读取的是图像的高度,shape[1]读取的是图像的宽度
# image_shape = image_np.shape

# 创建单通道的全零数组，此时需要创建一个与原图大小相同的单通道数组
# zeros:按照高和宽来创建的
# image_shape里面是全零数组，一个灰度图模块
# image_gray = np.zeros((image_shape[0],image_shape[1]),dtype=np.uint8)

# 定义一下权重
# weight_red = 0.299
# weight_green = 0.587
# weight_blue = 0.114

# 遍历彩色图像，彩色图像中的每个像素点都进行加权平均的操作
# 从而求出来每个像素点的灰度值，然后将得到的灰度值复制给image_gray
# 通过一个嵌套循环让我们能够遍历到我们所有图片中的所有像素点
# for i in range(image_shape[0]):
#     for j in range(image_shape[1]):
#         # 遍历到所有像素点之后，开始进行加权平均的计算
#         image_gray[i][j] = round(image_np[i,j][0] * weight_blue + image_np[i,j][1] * weight_green + image_np[i][j][2] * weight_red)
# 显示彩色图
cv2.imshow("image_np", image_np)
# 使用cv2.imshow()去显示image_gray
# cv2.imshow("image_gray", image_gray)
cv2.imshow("image_gray", cv_gray)
# 使用cv.2waitkey(0)将图像固定下来
cv2.waitKey(0)








