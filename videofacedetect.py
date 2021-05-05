import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(0.30)
pTime = 0
cap = cv.VideoCapture('Videos/mkbhd.mp4')


def Rescale(frame, scale=0.50):
    # FOR PICTURES,VIDEO,LIVE JUST T0 MAKE IT FIT
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def drawBorders(image, bbox, len=30, thick=4):
    x, y, w, h = bbox
    x1, y1 = x+w, y+h
    cv.line(image, (x, y), (x+len, y), (255, 0, 255), thick)
    cv.line(image, (x, y), (x, y+len), (255, 0, 255), thick)
    cv.line(image, (x1, y), (x1-len, y), (255, 0, 255), thick)
    cv.line(image, (x1, y), (x1, y+len), (255, 0, 255), thick)
    cv.line(image, (x, y1), (x+len, y1), (255, 0, 255), thick)
    cv.line(image, (x, y1), (x, y1-len), (255, 0, 255), thick)
    cv.line(image, (x1, y1), (x1-len, y1), (255, 0, 255), thick)
    cv.line(image, (x1, y1), (x1, y1-len), (255, 0, 255), thick)
    return image


while True:
    istrue, frame = cap.read()
    resize = Rescale(frame)
    RGB = cv.cvtColor(resize, cv.COLOR_BGR2RGB)
    results = faceDetection.process(RGB)
    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxc = detection.location_data.relative_bounding_box
            height, width = resize.shape[:2]
            bbox = int(bboxc.xmin * width), int(bboxc.ymin *
                                                height), int(bboxc.width * width), int(bboxc.height * height)
            cv.rectangle(resize, bbox, (255, 0, 255), 1)
            cv.putText(resize, f'{round(detection.score[0]*100)}%', (bbox[0],
                                                                     bbox[1]-20), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), thickness=1)
            resize = drawBorders(resize, bbox)
    cTime = time.time()
    fps = round(1/(cTime-pTime))
    pTime = cTime
    cv.putText(resize, f'FPS:{fps}', (20, 70),
               cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), thickness=1)
    cv.imshow('video', resize)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
