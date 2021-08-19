import cv2
import numpy as np 

# adding shapes and lines  to the images 

# zero means black 
# height, width, depth
img = np.zeros((512,512,3), np.uint8)

# all blue image
imgBlue = np.zeros((512,512,3), np.uint8)
# just colon is whole image
imgBlue[:]= 255,0,0

# part blue image
imgPartBlue = np.zeros((512,512,3), np.uint8)
# can select which pixels to edit
imgPartBlue[200:300,100:300]= 255,0,0

# create lines first give image, then starting and ending point
# then the color of the line and the thickness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

# create a rectangle in an image
# input image, and the two opposite corner, color and thicness
# use cv2.FILLED to fill the rectangle
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)

# create a circle in a rectangle
# input center and radius, then color and thickness of line
cv2.circle(img,(450,50),30,(255,255,0),4)

# add text to an image
# the string to add and the the origin of where to place it
# then the font scale and color and thickness
cv2.putText(img," OpenCV ", (300,100), cv2.FONT_HERSHEY_COMPLEX,1,
(0,150,0),1)

cv2.imshow("Image Line, Rectangle, Circle, and Text", img)
#cv2.imshow("Blue Image", imgBlue)
#cv2.imshow("Part Blue Image", imgPartBlue)

cv2.waitKey(0)