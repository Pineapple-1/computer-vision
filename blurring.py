import cv2 as cv

CATS = cv.imread('Photos/CATS.jpg')
# AVG BLUR
AVG = cv.blur(CATS,(3,3))

# GAUSSION BLUR MORE NATURAL THEN AVG BLUR
GAUSSION = cv.GaussianBlur(CATS,(3,3),0)

# Median blur almost same thing as AVG but it takes median rather then average so it is better in reducing noise

MEDIAN = cv.medianBlur(CATS,3)

# bilateral blurring it is the most effective blurring method.

BI = cv.bilateralFilter(CATS,5,15,15)

cv.imshow('BI',BI)
cv.imshow('MEDIAN',MEDIAN)
cv.imshow('AVG',AVG)
cv.imshow('GAUSSION',GAUSSION)
cv.imshow('CATS',CATS)
cv.waitKey(0)