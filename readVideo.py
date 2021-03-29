import cv2 as cv
vid = cv.VideoCapture('Videos/dog.mp4')
while True:
    istrue, frame = vid.read()
    cv.imshow('dog', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
