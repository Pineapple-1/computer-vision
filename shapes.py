import numpy as np
import cv2
import matplotlib.pyplot as plt

colors = ['green', 'orange', 'brown', 'dodgerblue', 'red', 'blue']
image = cv2.imread("Photos\objects.png", 0)

(thresh, binary) = cv2.threshold(image, 90, 255, cv2.THRESH_BINARY)
kernel = np.ones((10, 60), np.uint8)
dilate = cv2.dilate(binary, kernel, iterations = 1)

n_components, labels, stats, centroids = cv2.connectedComponentsWithStats(dilate, connectivity = 8)
output = image.copy()
for i in range(1, n_components):
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]    
    row = image[y:y+h-1, x:x+w-1]
    n_components1, labels1, stats1, centroids1 = cv2.connectedComponentsWithStats(row, connectivity = 8)
    for j in range(1, n_components1):
        x1 = stats1[j, cv2.CC_STAT_LEFT]
        y1 = stats1[j, cv2.CC_STAT_TOP]
        w1 = stats1[j, cv2.CC_STAT_WIDTH]
        h1 = stats1[j, cv2.CC_STAT_HEIGHT]
        
        cv2.rectangle(output, (x + x1, y + y1), (x + x1 + w1, y + y1 + h1), (255, 0, 255), 2)
        plt.scatter(w1, h1, c = y, cmap = plt.cm.Set1, edgecolor = colors[i-1])


cv2.imshow('output',output)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
