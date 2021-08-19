import cv2
import numpy as np

# edge detection and color conversion

img = cv2.imread("Resources/lena.png")

# 5 by 5 matrix one ones, values are ints from 0-255
kernel = np.ones((5,5), np.uint8)

# converts image to different colors spaces
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blurr the image, kernal size must be odd numbers
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

# edge detection, higher number means less edges
imgCanny = cv2.Canny(img,150,200)

#image dialation, make edges thicker 
# have to add a kernel: a matrix 
# iterations is how many times we go over the image
# the thickness of edges increases with number of iterations
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# eroded function is opposite of dialation, makes edges skinnier
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

#shows image, title and then the image
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)