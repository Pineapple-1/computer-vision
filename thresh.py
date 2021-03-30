import cv2 as cv
COINS = cv.imread('Photos/coins.png')
# TURN IT TO GRAY OTHER WISE IT WONT WORK FOR SOME THINGS SO I SUGGEST YOU GRAY IT
GRAY = cv.cvtColor(COINS, cv.COLOR_BGR2GRAY)
# we have to find threshold first
REC,THRESH = cv.threshold(GRAY, 95, 255, cv.THRESH_BINARY)
cv.imshow('THRESH',THRESH)
cv.waitKey(0)
