import cv2 as cv
import numpy as np
PARK = cv.imread('Photos/park.jpg')
BLANK = np.zeros(PARK.shape[:2], dtype='uint8')
# we can split channels by using this
B, G, R = cv.split(PARK)
# we can merge those split channels and merge them together
MERGE = cv.merge([B, G, R])
# so that we can see the color distribution vissually
BLUE = cv.merge([B, BLANK, BLANK])
GREEN = cv.merge([BLANK, G,BLANK])
RED = cv.merge([BLANK,BLANK, R])


cv.imshow('BLUE', BLUE)
cv.imshow('GREEN', GREEN)
cv.imshow('RED', RED)
cv.imshow('PARK', PARK)
cv.waitKey(0)
