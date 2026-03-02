import cv2

image = cv2.imread("../10000.jpg")

image_median = cv2.medianBlur(image, 5)


cv2.imshow("image",image)
cv2.imshow("image_median",image_median)
cv2.waitKey(0)
