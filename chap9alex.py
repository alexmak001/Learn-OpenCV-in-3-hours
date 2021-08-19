import cv2

# get pretained model to find faces
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# finds all faces in the image, chang the parameters based on results
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

# create a bounding box around all the faces detected
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0))

cv2.imshow("Result", img)

cv2.waitKey(0)