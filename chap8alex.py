import cv2
import numpy as np

# contour detection

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# function for contours
def getContours(img):
    # first input the image and then the method of retreivel
    # Retr_external retrievez the extreme outter contours
    contours, heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        # find area of contours 
        area = cv2.contourArea(cnt)
        print(area)
        
        # prevents noise from being classified
        if area > 500:
            # draws the contours on the image
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)

            # find length in order to locate object
            # true signifies shapes are closed
            perimeter = cv2.arcLength(cnt,True)
            print(perimeter)

            # play around with number to find which works best
            # true signifies shape is closed
            # gives coordinates of the shape
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter,True)
            print(len(approx))

            # corners for objects
            objCor = len(approx)
            x, y, width, height =  cv2.boundingRect(approx)

            if objCor == 3:
                ObjectType = "Triangle"
            elif objCor == 4:
                # need to differentiate between square and rectangle
                aspectRatio = width/float(height)
                if aspectRatio > 0.95 and aspectRatio < 1.05:
                    ObjectType = "Square"
                else:
                    ObjectType = "Rectangle"
            elif objCor > 4:
                ObjectType = "Circle"
            else:
                ObjectType = "other"
            # draw the corners
            cv2.rectangle(imgContour,(x,y),(x+width,y+height),(0,255,0),2)
            # write the labels
            cv2.putText(imgContour, ObjectType,
                    (x+(width//2)-10,y+(height//2)-10),cv2.FONT_HERSHEY_COMPLEX,
                    0.7,(0,0,0),2)

path = "Resources/shapes.png"
img = cv2.imread(path)
# copy image for drawing contours
imgContour = img.copy()

# convert to gray scale and blur
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)

# find edges
imgCanny = cv2.Canny(imgBlur,50,50)

# blank image with all zeroes
imgBlank = np.zeros_like(img)

getContours(imgCanny)
imgStack = stackImages(0.8,([img,imgGray,imgBlur],
[imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)
