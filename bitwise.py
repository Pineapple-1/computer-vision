import cv2 as cv
import numpy as np

BLANK = np.zeros((400, 400), dtype='uint8')

REC = cv.rectangle(BLANK.copy(), (30, 30), (370, 370), 255, -1)
CIRCLE = cv.circle(BLANK.copy(), (200, 200), 200, 255, -1)
# BITWISE AND IT RETURNS INTERSECTION
AND = cv.bitwise_and(REC, CIRCLE)
# BITWISE OR IT RETURNS INTERSECTING AND NON INTERSECTION REGIONS
OR = cv.bitwise_or(REC, CIRCLE)
# BITWISE XOR IT RETURNS NON INTERSECTION REGIONS
XOR = cv.bitwise_xor(REC, CIRCLE)

# BITWISE NOT IT RETURNS IT INVERTS BINARY COLORS
NOT = cv.bitwise_not(REC, CIRCLE)

cv.imshow("NOT", NOT)
cv.imshow("XOR", XOR)
cv.imshow("AND", AND)
cv.imshow("OR", OR)

cv.waitKey(0)
