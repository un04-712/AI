import cv2

image = cv2.imread("../10000.jpg")

# image_box = cv2.boxFilter(image,-1,(3,3),normalize=False)
image_box = cv2.boxFilter(image,-1,(3,3))
cv2.imshow("image",image)
cv2.imshow("image_box",image_box)
cv2.waitKey(0)