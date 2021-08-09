import os
import numpy as np
import cv2 as cv


PEOPLE = ['Ben Afflek', 'Elton John',
          'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
HARR_CASSCADE = cv.CascadeClassifier('harr_face.xml')
DIR = r'Faces\train'
features = []
label = []


def train():
    for PERSON in PEOPLE:
        PATH = os.path.join(DIR, PERSON)
        LABLE = PEOPLE.index(PERSON)
        for IMG in os.listdir(PATH):
            IMG_PATH = os.path.join(PATH, IMG)
            IMG_ARRAY = cv.imread(IMG_PATH)
            GRAY_ARRAY = cv.cvtColor(IMG_ARRAY, cv.COLOR_BGR2GRAY)
            FACE = HARR_CASSCADE.detectMultiScale(GRAY_ARRAY, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, z) in FACE:
                FACES = GRAY_ARRAY[y:y+z, x:x+w]
                features.append(FACES)
                label.append(LABLE)


train()
features = np.array(features, dtype=object)
label = np.array(label)
face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.train(features, label)
face_recogniser.save('face_trained.yml')
np.save('features.npy', features)
np.save('label.npy', label)
