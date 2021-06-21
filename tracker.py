import cv2 as cv
import matplotlib.pyplot as plt
import math
cap = cv.VideoCapture('Videos\Pendulum.avi')
ret, frame = cap.read()
prevframe = frame    #First frame
magnitude = []
prevavg =[159.5 ,119.5]
while True:
    ret, frame = cap.read()
    nextframe = frame
    if ret:
        diff = cv.absdiff(prevframe,nextframe)
        diff = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
        kernal = cv.getStructuringElement(cv.MORPH_ELLIPSE,(7,7))
        diff = cv.morphologyEx(diff,cv.MORPH_OPEN, kernal)
        _,ret = cv.threshold(diff,40,255,cv.THRESH_BINARY)
        n_components, labels, stats, centroids = cv.connectedComponentsWithStats(ret,8,cv.CV_32S)
        avg  = (sum(centroids) / len(centroids))
        vx = abs(avg[0]-prevavg[0])/(1/30)
        vy = abs(avg[1]-prevavg[1])/(1/30)
        magnitude.append(math.sqrt(vx**2+vy**2))
        print(magnitude)
        prevavg = avg
        cv.imshow('video', ret)
        prevframe = nextframe   #Frame difference method Background change
        if cv.waitKey(30) & 0xff == ord('d'):
            break
    else:
        break
    
plt.plot(range(1,500),magnitude)
plt.show()
cv.destroyAllWindows()
cap.release()