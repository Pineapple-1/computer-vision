import cv2 as cv
import matplotlib.pyplot as plt
CATS =cv.imread('Photos/cats 2.jpg')
GRAY = cv.cvtColor(CATS,cv.COLOR_BGR2GRAY)
GRAY_HIST= cv.calcHist([CATS],[2],None,[256],[0,255])
plt.figure()
plt.title('HISTOGRAM')
plt.xlabel('BINS')
plt.ylabel('# of pixels')
plt.plot(GRAY_HIST)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)