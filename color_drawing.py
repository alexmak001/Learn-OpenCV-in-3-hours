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
# first is green marker 
# second is red, and third is black marker
myColors = [[57,117,22,89,255,174], 
[0,149,53,4,235,128],
[0,0,0,179,173,12]]

#BGR values
myColorValues = [[0,255,0],
[0,0,255],
[0,0,0]]

myPoints = [] 
#[x,y, colorId] x and y are coordinates and color ID is color values

def findColor(img, myColor, myColorValue):
    # finds the edges in the image
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    # show window for each color
    for color in myColor:
        # creating a mask that is in the range of the colors
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)

        # get the Contours
        x,y = getContours(mask)
        # draw a circle around the point 
        # image to draw it too, center, radion, color
        cv2.circle(imgResult,(x,y), 10, myColorValue[count], cv2.FILLED)
        #cv2.imshow(str(color[1]), mask)

        if x!=0 and y!=0:
            newPoints.append([x,y,count])

        count += 1
    return newPoints


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # draw from tip not center
    # return the middle point and top
    return x+w//2,y 


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    # shows the camera image
    success, img = cap.read()

    # final image with all of the drawings
    imgResult = img.copy()

    newPoints = findColor(img, myColors, myColorValues)

    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(newPoints)!=0:
        drawOnCanvas(myPoints, myColorValues)

    
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break