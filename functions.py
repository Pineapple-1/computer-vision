import cv2 as cv
CAT = cv.imread('Photos/cat.jpg')
PARK = cv.imread('Photos/park.jpg')
GRAY = cv.cvtColor(CAT, cv.COLOR_BGR2GRAY)
# blur to reduce noise
BLUR = cv.GaussianBlur(PARK, (3, 3), cv.BORDER_DEFAULT)
# edge casscading (reducing edges by blurring)
CANNY = cv.Canny(BLUR, 170, 255)
# dilating the image (more visibility of edges but loss of small edges) it soften the edges
DILATE = cv.dilate(CANNY, (3, 3), iterations=2)
# eroding image (if we erode a dilated image in most of cases it will go back to casscaded image)
ERODE = cv.erode(DILATE, (3, 3), iterations=2)
# Resize so interpolation is when you are resizing it to larger image cubic will take time
RESIZE = cv.resize(PARK, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('PARK', PARK)
cv.imshow('CANNY', CANNY)
cv.imshow('DILATE', DILATE)
cv.imshow('ERODE', ERODE)
cv.imshow('RESIZE', RESIZE)
cv.waitKey(0)
