import cv2 as cv

HARR_CASSCADE = cv.CascadeClassifier('harr.xml')
PEOPLE = ['Ben Afflek', 'Elton John','Jerry Seinfield', 'Madonna', 'Mindy Kaling']

face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.read('face_trained.yml')
image = cv.imread('Photos/lady.jpg')
cv.imshow('gray',image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

face_rect = HARR_CASSCADE.detectMultiScale(gray, 1.1, 4)
for (x,y,w,z) in face_rect:
    face_roi = gray[y:y+z,x:x+w]
    
    lable , confidence = face_recogniser.predict(face_roi)
    print(confidence)
    cv.putText(image, str(PEOPLE[lable]), (x,z),cv.FONT_HERSHEY_PLAIN,1.0,(0,255,0),thickness=2)
    cv.rectangle(image,(x,y),(x+w,y+z),(0,225,0),thickness=2)
    
cv.imshow('RECOGNIZER',image)
cv.waitKey(0)