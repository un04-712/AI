import cv2
image = cv2.imread("../10000.jpg")

image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# ret,image_thresh = cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY)

image_Gaussian = cv2.GaussianBlur(image_gray,(5,5),0)

image_canny = cv2.Canny(image_Gaussian,100,200)

cv2.imshow("Canny",image_canny)
cv2.waitKey(0)
