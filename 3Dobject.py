import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_objectron = mp.solutions.objectron
objectron=mp_objectron.Objectron(static_image_mode=True,max_num_objects=5,min_detection_confidence=0.5,model_name='Shoe')

drawSpecs = mp_drawing.DrawingSpec(color= (200,220,140),thickness=2, circle_radius=1)
file_list = ['Photos\kmodo.JPG','Photos\sneeker.JPG','Photos/nike.jpg','Photos\chair.jpg']
def Rescale(frame, scale=0.75):
    # FOR PICTURES,VIDEO,LIVE
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

image = cv2.imread(file_list[0])

    # Convert the BGR image to RGB and process it with MediaPipe Objectron.
results = objectron.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # Draw box landmarks.
if not results.detected_objects:
    print(f'No box landmarks detected on {file_list[0]}')
else:
    print(f'Box landmarks of {file_list[0]}:')
    annotated_image = image.copy()
    print(results.detected_objects)

    for detected_object in results.detected_objects:
        mp_drawing.draw_landmarks(annotated_image, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS,drawSpecs,drawSpecs)
    cv2.imshow('Images', annotated_image)
    cv2.waitKey(0)
