import cv2

image = cv2.imread('../10000.jpg')

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_sobel = cv2.Sobel(image_gray, -1, 0, 1)

cv2.imshow('Sobel', image_sobel)
cv2.waitKey(0)