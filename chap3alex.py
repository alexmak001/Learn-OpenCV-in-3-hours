import cv2
import numpy as np 

# resizing and cropping images

img = cv2.imread("Resources/lambo.png")

# shape gives height, width, depth in that order
print(img.shape)

#give image and then give the new desired width and height in the order
imgResize = cv2.resize(img, (1000,500)) #(width, height)
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)