import cv2 as cv
import numpy as np
cameraman = cv.imread('./Photos/cameraman.tif')
saturn = cv.imread('./Photos/saturn.png')
saturn = cv.resize(saturn, (cameraman.shape[0], cameraman.shape[1]), interpolation=cv.INTER_AREA)
# we can split channels by using this
cameraman = cv.cvtColor(cameraman,cv.COLOR_BGR2GRAY)
b, g, r = cv.split(saturn)
r = r >> 2
r = r << 2
g = g >> 2
g = g << 2
b = b >> 2
b = b << 2
cr = cameraman >> 6
cg = cameraman << 2
cg = cg >> 6
cb = cameraman << 4
cb= cb >> 6
# bitwise or perfoms 
r =  cv.bitwise_or(r, cr)
g = cv.bitwise_or(g, cg)
b = cv.bitwise_or(b, cb)
merged = cv.merge([b,g,r])
b,g,r=cv.split(merged)
redpart = r<<6
greenpart = g<<6
greenpart = greenpart>>2
bluepart= b<<6
bluepart = b>>4
# if we use bit wise or here the imgae gets distorted.
# if we use merge here the image gets red.
image=bluepart|greenpart|redpart
cv.imshow('saturn',merged)
cv.imshow('hiddenimage',image)
cv.waitKey(0)
