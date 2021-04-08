import cv2 as cv
import numpy as np
# so contures are boundaries of the image sooo.
# you can say that these are edges but they are not edges.
# but programing point of view they are edges.
CATS = cv.imread('photos/cats.jpg')
BLANK = np.zeros(CATS.shape, dtype='uint8')
cv.imshow('Cat', CATS)
Gray = cv.cvtColor(CATS, cv.COLOR_BGR2GRAY)
BLUR = cv.GaussianBlur(CATS, (5, 5), cv.BORDER_DEFAULT)
Canny = cv.Canny(BLUR, 125, 175)
ret, thresh = cv.threshold(Gray, 125, 225, cv.THRESH_BINARY)
# we can also do it with thresholded image sooo we can find contures with canny edges and thresh
Contours, Hierarchies = cv.findContours(
    Canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(BLANK, Contours, -1, (0, 0, 225))
print(f'{len(Contours)} contours found')
cv.imshow('Gray', Gray)
cv.imshow('CANNY', Canny)
cv.imshow('Draw Contours', BLANK)
cv.waitKey(0)
