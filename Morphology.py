import cv2 as cv
import numpy as np

eight = cv.imread('Photos\eight.png')
ship = cv.imread('Photos\spaceship.png')
lines = cv.imread('Photos\lines.png')
img = cv.imread('Photos/abstract.png', cv.IMREAD_GRAYSCALE)
def myMorphology(img):
    GRAY = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    VAL,THRESH = cv.threshold(GRAY, 190, 255, cv.THRESH_BINARY)
    THRESH  = 255 - THRESH
    kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    closing = cv.morphologyEx(THRESH , cv.MORPH_CLOSE,kernel)
    erosion = cv.erode(closing ,kernel,iterations = 1)
    final = THRESH - erosion
    return final
val, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
thresh = 255 - thresh
kernel = np.ones((3, 7), dtype=np.uint8)
n_components, labels, stats, centroids = cv.connectedComponentsWithStats(cv.dilate(thresh, kernel), connectivity=4)
print("WORDS: ",(n_components - 1))
kernel = np.ones((3, 28), dtype=np.uint8) 
n_components, labels, stats, centroids = cv.connectedComponentsWithStats(cv.dilate(thresh, kernel), connectivity=8)
print("LINES: ",(n_components - 1))
kernel = np.ones((6,11),np.uint8)
verticallines = cv.morphologyEx(lines, cv.MORPH_OPEN,kernel)
kernel = np.ones((11,6),np.uint8)
horizontallines = cv.morphologyEx(lines, cv.MORPH_OPEN,kernel)
kernel= cv.getStructuringElement(cv.MORPH_ELLIPSE,(10,10))
spaceship= cv.morphologyEx(ship ,cv.MORPH_CLOSE,kernel)
cv.imshow('mymorph',myMorphology(eight))
cv.imshow('spaceship',spaceship )
cv.imshow('verticallines', verticallines)
cv.imshow('horizontallines',horizontallines )
cv.waitKey(0)
