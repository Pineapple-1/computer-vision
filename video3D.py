import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron
drawSpecs = mp_drawing .DrawingSpec(
    color=(200, 220, 140), thickness=2, circle_radius=1)


def Rescale(frame, scale=0.75):
    # FOR PICTURES,VIDEO,LIVE
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


cap = cv2.VideoCapture('Videos\shoes.mp4')
with mp_objectron.Objectron(static_image_mode=False, max_num_objects=4,min_detection_confidence=0.6, min_tracking_confidence=0.5, model_name='Shoe') as objectron:
    while True:
        success, image = cap.read()

        # Convert the BGR image to RGB.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = objectron.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                    image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS, drawSpecs, drawSpecs)
        cv2.imshow('MediaPipe Objectron', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
