import numpy as np
import cv2
import argparse
from matplotlib import pyplot as plt


scr = cv2.imread('../Images/dibujo01.png')
# scr = cv2.imread('../Images/test01.jpg')

gray = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)

# noise removal
kernel = np.ones((3, 3), np.uint8)
gray_filtered = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=3)

gmax = np.max(np.max(gray))
gmed = np.average(gray)
gdev = np.sqrt(np.var(gray))

# print(gmed, gdev)
# umbral = gmax - (gmed + 0.5*gdev)
# drawn[gray < gmed-umbral] = 0
# ret, thresh = cv2.threshold(gray, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

thresh = cv2.adaptiveThreshold(gray_filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 315, gdev/2)
thresh_median= cv2.medianBlur(thresh, 3)

# Dilating image
dilated = cv2.dilate(thresh_median, kernel, iterations=5)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(dilated, cv2.DIST_L12, 0)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(dilated, sure_fg)

cv2.imshow("Source", scr)
cv2.imshow("Result", dilated)


#
# # Marker labelling
# ret, markers = cv2.connectedComponents(sure_fg)
#
# # Add one to all labels so that sure background is not 0, but 1
# markers = markers+1
#
# # Now, mark the region of unknown with zero
# markers[unknown > 10] = -1
#
# markers = cv2.watershed(scr, markers)
#
# print(np.shape(scr))
# print(markers)
# zones = 255*np.ones(np.shape(scr))
#
# zones[markers == -1] = [255, 0, 0]
#
#
#




cv2.waitKey(0)

cv2.destroyAllWindows()
