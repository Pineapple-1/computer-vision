import cv2 as cv
import mediapipe as mp
cap = cv.VideoCapture('Videos/data.mp4')
while True:
    istrue, frame = cap.read()
    cv.imshow('dog', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break