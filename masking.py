# FOR FOCUSING ANY THING WE USE MASKING
import cv2 as cv
import numpy as np
CATS=cv.imread('Photos/cats.jpg')
# IMPORTANT MASK IMAGE AND OTHER SHOULD HAVE THE SAME DIMENSIONS OTHER WISE IT WONT WORK
BLANK = np.zeros(CATS.shape[:2],dtype='uint8')
# WE CAN ALSO DO THIS WITH OTHER SHAPES
MASK = cv.circle(BLANK,(CATS.shape[1]//2,CATS.shape[0]//2),160,255,-1)
# MASKED IMAGE 
MASKIMG = cv.bitwise_and(CATS,CATS,mask=MASK)

cv.imshow('MASKED',MASKIMG)
cv.imshow('MASK',MASK)
cv.imshow('CATS',CATS)
cv.waitKey(0)
