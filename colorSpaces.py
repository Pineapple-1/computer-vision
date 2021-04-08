# color spaces represent color of any array
import cv2 as cv
PARK = cv.imread('Photos/park.jpg')
# by deafault open cv reads image to BGR

#  BGR TO GRAY
GRAY = cv.cvtColor(PARK, cv.COLOR_BGR2GRAY)

# BGR TO HSV = HUE SATURATION VALUE
HSV = cv.cvtColor(PARK, cv.COLOR_BGR2HSV)

# BGR TO L*A*B HOW HUMANS PRECIVE COLORS
LAB = cv.cvtColor(PARK, cv.COLOR_BGR2LAB)

# BGR TO RGB
RGB = cv.cvtColor(PARK, cv.COLOR_BGR2RGB)

# HSV TO BGR
HSVTOBGR = cv.cvtColor(HSV, cv.COLOR_HSV2BGR)
cv.imshow('HSVTOBGR', HSVTOBGR)
cv.imshow('RGB', RGB)
cv.imshow('LAB', LAB)
cv.imshow('HSV', HSV)
cv.imshow('GRAY', GRAY)
cv.imshow('Park', PARK)
cv.waitKey(0)
