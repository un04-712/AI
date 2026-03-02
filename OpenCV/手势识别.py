# 肤色分割→轮廓提取→凸包与凸缺陷分析→手指计数

"""
        先通过 HSV 颜色范围分离肤色，再用形态学操作优化肤色区域；
        从优化后的区域中提取手的轮廓，并计算其凸包；
        分析凸包与轮廓的凹陷（凸缺陷），通过凹陷处的角度判断手指缝，最终反推手指数量。
"""
import cv2
import numpy as np

image = cv2.imread("./img_1.png")
image_copy = image.copy()
# 转化成hsv
hsv = cv2.cvtColor(image_copy, cv2.COLOR_BGR2HSV)

# 定义肤色范围
lower = np.array([0, 20, 70], np.uint8)
upper = np.array([20, 255, 255], np.uint8)

# 制作掩膜
mask = cv2.inRange(hsv, lower, upper)

# 形态学操作
kernel = np.ones((5, 5), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=4)
mask = cv2.erode(mask, kernel, iterations=2)

cv2.imshow("mask",mask)

# 查找图像轮廓
contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制图像轮廓
image_con = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# cv2.imshow("image_con",image_con)
# cv2.waitKey(0)

# 计算凸包
# 凸包点坐标（用于画图）
hull_points = cv2.convexHull(contours, returnPoints=True)
# 凸包点索引（用于凸缺陷计算）
hull_idx = cv2.convexHull(contours, returnPoints=False)

image_hull = cv2.polylines(image_copy, [hull_points], True, (0, 0, 255))
# cv2.imshow('image_hull', image_hull)
# 计算凸缺陷
defects = cv2.convexityDefects(contours, hull_idx)

if defects is not None:
    # 计算手指数量
    finger_count = 0

    for i in range(defects.shape[0]):  # 遍历每个缺陷点
        s, e, f, d = defects[i, 0]
        start = tuple(contours[s][0])  # 缺陷起点坐标
        end = tuple(contours[e][0])    # 缺陷终点坐标
        far = tuple(contours[f][0])    # 缺陷最深处的点坐标

        #缺陷起点  缺陷终点  缺陷最深处的点 三个点构成一个三角形
        #计算start-end far-start  end-far 三个边长
        a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

        # 计算角度 根据余弦定理计算出start-far far-end 两个边之间的夹角  cos(θ) = (b^2+c^2-a^2)/2bc
        angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180 / np.pi
#
        # 如果角度小于90度，则认为是手指间的凹陷
        if angle < 90:
            finger_count += 1
            cv2.circle(image_copy, far, 5, [68, 147, 245], -1)

    # 手指数量需要加1（因为缺陷数量比手指数量少1） 这样也会导致只要检测到轮廓时，就会显示1
    finger_count += 1
    cv2.putText(image_copy, f"Fingers: {finger_count}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


# 显示结果
cv2.imshow('Gesture Recognition', image_copy)

cv2.waitKey(0)
