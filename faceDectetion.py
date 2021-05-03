import cv2 as cv
PERSON =cv.imread('Photos/group 1.jpg')
GRAY = cv.cvtColor(PERSON,cv.COLOR_BGR2GRAY)
HARR_CASSCADE= cv.CascadeClassifier('harr_face.xml')
FACE =  HARR_CASSCADE.detectMultiScale(GRAY,scaleFactor=1.1,minNeighbors=1)
for (x,y,w,z) in FACE:
    cv.rectangle(PERSON,(x,y),(x+w,y+z),(0,225,0),thickness=2)
cv.imshow('PERSON',PERSON)
cv.waitKey(0)
