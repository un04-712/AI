import cv2

image = cv2.imread('../10000.jpg')


image_laplacian = cv2.Laplacian(image, -1)

cv2.imshow('Laplacian', image_laplacian)
cv2.waitKey(0)