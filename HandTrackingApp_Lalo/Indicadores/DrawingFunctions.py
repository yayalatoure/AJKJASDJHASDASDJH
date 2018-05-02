import numpy as np
import cv2


def UsedSpace(scr):

    gray = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)

    # noise removal Erosion then Dilation
    kernel = np.ones((3, 3), np.uint8)
    gray_filtered = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)

    gdev = np.sqrt(np.var(gray))

    thresh = cv2.adaptiveThreshold(gray_filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 315, gdev/2)
    thresh_median = cv2.medianBlur(thresh, 1)

    kernel = np.ones((6, 6), np.uint8)
    closing = cv2.morphologyEx(thresh_median, cv2.MORPH_CLOSE, kernel)

    # Dilating image
    dilated = cv2.dilate(closing, kernel, iterations=1)

    # Copy the thresholded image.
    im_floodfill = dilated.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = dilated.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0, 0), 255);

    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    # Combine the two images to get the foreground.
    im_flood_dil = dilated | im_floodfill_inv

    kernel = np.ones((3, 3), np.uint8)
    eroded = cv2.erode(im_flood_dil, kernel, iterations=1)


    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(eroded, connectivity=8)

    sizes = stats[0:, -1]
    nb_components = nb_components - 1
    min_size = 250

    area_filtered = np.zeros(output.shape)
    for i in range(0, nb_components):
        if sizes[i] >= min_size:
            area_filtered[output == i + 1] = 255

    output = area_filtered

    # # Display images.
    cv2.imshow("Original", scr)
    cv2.imshow("Gray Filtered", gray_filtered)
    cv2.imshow("Adaptive Threshold", thresh)
    cv2.imshow("Median Filter Threshold", thresh_median)
    cv2.imshow("Erotion and Dilatation", eroded)
    cv2.imshow("Used Area", output)


    h, w = output.shape
    usedPixels = np.sum(np.sum(output))/255
    area = (usedPixels/(h*w))*100

    print 'Area Utilizada: %.2f' % area

    return output, area
