import cv2 as cv
import time
COINS = cv.imread('Photos/coins.png')
# TURN IT TO GRAY OTHER WISE IT WONT WORK
GRAY = cv.cvtColor(COINS, cv.COLOR_BGR2GRAY)
# BLUR IT IF YOU WANT FOR MORE CLEAR BINARY IMAGE
GAUSSION = cv.GaussianBlur(GRAY,(3,3),0)
# YOU CAN USE BLURED IMAGE OR NORMAL
REC,THRESH = cv.threshold(GAUSSION , 95, 255, cv.THRESH_BINARY)
# CONNECTED COMPONENTS TAKES BINARY IMAGE , CONNECTIVITY (4 OR 8) 
n_components, labels, stats, centroids = cv.connectedComponentsWithStats(THRESH,8,cv.CV_32S)
for x in range(1,11): 
    diameter = stats[x, cv.CC_STAT_WIDTH]
    cv.circle(COINS,(int(centroids[x][0]),int(centroids[x][1])),diameter//2,(0,220,0),thickness=2)
    cv.line(COINS,(int(centroids[1][0]),int(centroids[1][1])),(int(centroids[x][0]),int(centroids[x][1])), (255,0,0),thickness=1)
    cv.putText(COINS, str(x),(int(centroids[x][0]),int(centroids[x][1])), cv.FONT_HERSHEY_TRIPLEX,1, (50, 50, 50), thickness=2)
cv.imshow('coins',COINS)
cv.imshow('thresh',THRESH)
cv.waitKey(0)

 