import cv2 as cv
import numpy as np
PARK = cv.imread('photos/park.jpg')


def translate(PARK, x, y):

    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (PARK.shape[1], PARK.shape[0])
    return cv.warpAffine(PARK, transMat, dimensions)


# driections according to values
# -x = left
# x = right
# -y = up
# y = down


def rotate(PARK, angle, rotationPoint=None):
    (height, width) = PARK.shape[:2]
    if rotationPoint == None:
        rotationPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (PARK.shape[1], PARK.shape[0])
    return cv.warpAffine(PARK, rotMat, dimensions)

# flip creates mirror effect 0 will flip it upside down
# 1 will mirror it like horizontoly (like iphone main camera)
# -1 will it will do both upside down and horizontlly


flip0 = cv.flip(PARK, 0)
flip1 = cv.flip(PARK, 1)
flip_1 = cv.flip(PARK, -1)
cv.imshow('original', PARK)
cv.imshow('flip0', flip0)
cv.imshow('flip1', flip1)
cv.imshow('flip-1', flip_1)

cv.waitKey(0)
