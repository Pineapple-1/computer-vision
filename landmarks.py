import cv2 as cv
import mediapipe as mp
import time


mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpecs = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
cap = cv.VideoCapture('Videos/mkbhd.mp4')

pTime = 0


def Rescale(frame, scale=0.50):
    # FOR PICTURES,VIDEO,LIVE JUST T0 MAKE IT FIT
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


while True:
    istrue, frame = cap.read()
    resize = Rescale(frame)
    RGB = cv.cvtColor(resize, cv.COLOR_BGR2RGB)
    results = faceMesh.process(RGB)
    if results.multi_face_landmarks:
        for facelms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(
                resize, facelms, mpFaceMesh.FACE_CONNECTIONS, drawSpecs, drawSpecs)
    cTime = time.time()
    fps = round(1/(cTime-pTime))
    pTime = cTime
    cv.putText(resize, f'FPS:{fps}', (20, 70),
               cv.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), thickness=1)
    cv.imshow('dog', resize)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break
