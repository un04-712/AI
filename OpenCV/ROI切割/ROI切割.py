import cv2

image = cv2.imread("../10000.jpg")
# image_shape = image.shape
# print(image_shape)
# 获取图像的高度和宽度
height,width = image.shape[0],image.shape[1]

# 切割感兴趣的区域
# 人为指定要切割的区域
try:
    x_min,x_max = 400,700
    y_min,y_max = 0,320

    if not (x_min >= 0 and x_max<=width and y_min >= 0 and y_max<=height):
        raise OverflowError("x_min or x_max or y_min or y_max overflow")
    #  使用cv2.rectangle去画一个矩形框，方便我们去调整感兴趣的区域的范围
    cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(255,180,103),2)

    # 使用np数组的切片操作，对图像进行切割
    image_roi = image[y_min:y_max,x_min:x_max]
    cv2.imshow("image",image)
    cv2.imshow("ROI",image_roi)
    cv2.waitKey(0)
except Exception as e:
    print(e)



