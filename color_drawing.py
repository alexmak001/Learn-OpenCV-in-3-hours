import cv2
import numpy as np

# sets the fram size
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
# ID for brightness is 10
cap.set(10,150)

# figure out my colors in a stable enviroment 
myColors = [[0,200,255, 10, 40,255], [87,231,11,98, 85,111]]


def findColor(img, myColors):
    # finds the edges in the image
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # creating a mask that is in the range of the colors
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHSV,lower,upper)
    cv2.imshow("img", mask)

while True:
    # shows the camera image
    success, img = cap.read()
    findColor(img, myColors)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break