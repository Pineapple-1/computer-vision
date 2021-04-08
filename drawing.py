import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
blank = np.zeros((500, 500, 3), dtype='uint8')

cv.rectangle(blank, (0, 0),
             (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
          40, (0, 0, 255), thickness=-1)
cv.line(blank, (0, 0),
        (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=2)
cv.putText(blank, 'hello', (100, 200), cv.FONT_HERSHEY_TRIPLEX,
           1, (50, 50, 50), thickness=2)
cv.imshow('blank', blank)

cv.waitKey(0)
