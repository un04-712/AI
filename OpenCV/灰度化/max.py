import cv2

import numpy as np

image_np  = cv2.imread(r"../10000.jpg")

image_shape = image_np.shape

image_gray = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)

for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        image_gray[i][j] = max(image_np[i,j][0], image_np[i,j][1], image_np[i,j][2])

cv2.imshow("image_gray", image_gray)
cv2.waitKey(0)