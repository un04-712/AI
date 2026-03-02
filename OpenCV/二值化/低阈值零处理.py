import cv2

image = cv2.imread("../10000.jpg")

cv_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh = 127
maxval = 255
ret,cv_thresh = cv2.threshold(cv_gray,thresh,maxval,cv2.THRESH_TOZERO)

# cv2.imshow('image',image)
# cv2.imshow('cv_gray',cv_gray)
cv2.imshow('cv_thresh',cv_thresh)
cv2.waitKey(0)