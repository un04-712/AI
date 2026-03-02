import cv2

image = cv2.imread("../10000.jpg")

image_filter = cv2.bilateralFilter(image,9,45,45)


cv2.imshow('image',image)
cv2.imshow("image_filter",image_filter)
cv2.waitKey(0)
