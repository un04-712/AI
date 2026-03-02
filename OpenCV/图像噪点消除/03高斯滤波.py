import cv2

image = cv2.imread("../10000.jpg")


image_Gaussian = cv2.GaussianBlur(image,(5,5),sigmaX=255,sigmaY=150)

cv2.imshow("image",image)
cv2.imshow("image_Gaussian",image_Gaussian)
cv2.waitKey(0)