import cv2 as cv
import numpy as np

Zebra = cv.imread('./Photos/zebra.png')
after_Zebra = cv.filter2D(Zebra, -1, 3)
Einstine = cv.imread('./Photos/blur.png')
kernel = np.array(([-1,-1,-1],[-1,9,-1],[-1,-1,-1]))
after_sharpen = cv.filter2D(Einstine,-1, kernel)
Coins =cv.imread('./Photos/bad.png')
medianBlur = cv.medianBlur(Coins,3)
red = cv.imread('./Photos/red.png')
BLANK = np.zeros(red.shape[:2], dtype='uint8')
B, G, R = cv.split(red)
RED = cv.merge([B,G,BLANK])
after_RED = ((RED/255)**(0.40))
Girl = cv.imread('./Photos/girl.png')
after_Girl =cv.filter2D(Girl, -1, 2)

cv.imshow('Girl',Girl)
cv.imshow('after_Girl',after_Girl)
cv.waitKey(0)
