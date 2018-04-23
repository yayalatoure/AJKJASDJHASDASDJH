import numpy as np
import cv2
import argparse

from matplotlib import pyplot as plt
from DrawingFunctions import *

# scr = cv2.imread('../Images/kd1.png')
scr = cv2.imread('../Images/kd3.jpg')


# gray = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)

# # noise removal
# kernel = np.ones((3, 3), np.uint8)
# gray_filtered = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)
#
# gmax = np.max(np.max(gray))
# gmed = np.average(gray)
# gdev = np.sqrt(np.var(gray))
#
# # print(gmed, gdev)
# # umbral = gmax - (gmed + 0.5*gdev)
# # drawn[gray < gmed-umbral] = 0
# # ret, thresh = cv2.threshold(gray, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#
# thresh = cv2.adaptiveThreshold(gray_filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 315, gdev/2)
# thresh_median = cv2.medianBlur(thresh, 3)
#
#
# kernel = np.ones((3, 3), np.uint8)
# erosion = cv2.erode(thresh_median, kernel, iterations=1)
#
#
# kernel = np.ones((5, 5), np.uint8)
# closing = cv2.morphologyEx(thresh_median, cv2.MORPH_CLOSE, kernel)
#
# # Dilating image
# dilated = cv2.dilate(closing, kernel, iterations=2)
#
#
# gradient = cv2.morphologyEx(thresh_median, cv2.MORPH_GRADIENT, kernel)
#
# # Finding sure foreground area
# dist_transform = cv2.distanceTransform(dilated, cv2.DIST_L12, 0)
# ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
#
# # Finding unknown region
# sure_fg = np.uint8(sure_fg)
# unknown = cv2.subtract(dilated, sure_fg)
#
# # cv2.imshow("Source", scr)
# # cv2.imshow("Gray Filtered", gray_filtered)
# # cv2.imshow("Erosion", erosion)
# # cv2.imshow("Closing", closing)
# # cv2.imshow("Gradient", gradient)
#
#
#
# im_th = dilated
#
# # Copy the thresholded image.
# im_floodfill = im_th.copy()
#
# # Mask used to flood filling.
# # Notice the size needs to be 2 pixels than the image.
# h, w = im_th.shape[:2]
# mask = np.zeros((h + 2, w + 2), np.uint8)
#
# # Floodfill from point (0, 0)
# cv2.floodFill(im_floodfill, mask, (0, 0), 255);
#
# # Invert floodfilled image
# im_floodfill_inv = cv2.bitwise_not(im_floodfill)
#
# # Combine the two images to get the foreground.
# im_out = im_th | im_floodfill_inv
#
# kernel = np.ones((3, 3), np.uint8)
# output = cv2.erode(im_out, kernel, iterations=1)
#
# # Display images.
# cv2.imshow("Thresholded Image", im_th)
# cv2.imshow("Floodfilled Image", im_floodfill)
# cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
# cv2.imshow("Foreground", output)

out, area = UsedSpace(scr)

cv2.waitKey(0)

cv2.destroyAllWindows()
