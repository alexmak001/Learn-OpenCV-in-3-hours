import cv2

minArea = 500
color = (255,0,255)


# get pretained model to find plate
plateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

for i in range(1,4):
    path = "Resources/p{0}.jpg".format(i)
    print(path)
    img = cv2.imread(path)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # finds all faces in the image, chang the parameters based on results
    numberPlates = plateCascade.detectMultiScale(imgGray,1.1,4)

    # create a bounding box around all the plates detected
    for (x,y,w,h) in numberPlates:
        # find the area and filter it
        area = w*h 

        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0))
            cv2.putText(img, "Number Plate",(x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)

            # get the license plate itself, gives region of number plate
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("Plate", imgRoi)

    cv2.imshow("Result", img)
    cv2.waitKey(0)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break