import numpy as np
import cv2
import matplotlib.pyplot as plt
import scipy


def UsedSpace(src):

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # noise removal Erosion then Dilation
    kernel = np.ones((2, 2), np.uint8)
    gray_filtered = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)

    edges = cv2.Canny(gray, 10, 10)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=2)



    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(dilated, connectivity=8)

    sizes = stats[0:, -1]
    nb_components = nb_components - 1
    min_size = 10

    area_filtered = np.zeros(output.shape)
    for i in range(0, nb_components):
        if sizes[i] >= min_size:
            area_filtered[output == i + 1] = 255

    develop = area_filtered




    ############################

    # gdev = np.sqrt(np.var(gray))
    #
    # thresh = cv2.adaptiveThreshold(gray_filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 315, gdev/3)
    # thresh_median = cv2.medianBlur(thresh, 3)
    #
    # kernel = np.ones((6, 6), np.uint8)
    # closing = cv2.morphologyEx(thresh_median, cv2.MORPH_CLOSE, kernel)

    # Dilating image
    # dilated = cv2.dilate(closing, kernel, iterations=2)

    # # Copy the thresholded image.
    # im_floodfill = dilated.copy()
    #
    # # Mask used to flood filling.
    # # Notice the size needs to be 2 pixels than the image.
    # h, w = dilated.shape[:2]
    # mask = np.zeros((h + 2, w + 2), np.uint8)
    #
    # # Floodfill from point (0, 0)
    # cv2.floodFill(im_floodfill, mask, (0, 0), 255);
    #
    # # Invert floodfilled image
    # im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    #
    # # Combine the two images to get the foreground.
    # im_flood_dil = dilated | im_floodfill_inv
    #
    # kernel = np.ones((2, 2), np.uint8)
    # eroded = cv2.erode(im_flood_dil, kernel, iterations=1)
    #
    # nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(eroded, connectivity=8)
    #
    # sizes = stats[0:, -1]
    # nb_components = nb_components - 1
    # min_size = 50
    #
    # area_filtered = np.zeros(output.shape)
    # for i in range(0, nb_components):
    #     if sizes[i] >= min_size:
    #         area_filtered[output == i + 1] = 255

    # output = np.uint8(area_filtered)
    #
    # kernel = np.ones((8, 8), np.uint8)
    # area_filtered = cv2.morphologyEx(output, cv2.MORPH_OPEN, kernel, iterations=3)

    # Display images.
    # cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Development", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("Gray Filtered", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("Adaptive Threshold", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("Median Filter Threshold", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("Erotion and Dilatation", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("Used Area", cv2.WINDOW_NORMAL)


    cv2.imshow("Develop", develop)
    # cv2.imshow("Original", src)
    # cv2.imshow("Gray Filtered", gray_filtered)
    # cv2.imshow("Adaptive Threshold", thresh)
    # cv2.imshow("Median Filter Threshold", thresh_median)
    # cv2.imshow("Erotion and Dilatation", eroded)
    # cv2.imshow("Used Area", area_filtered)


    # h, w = output.shape
    # usedPixels = np.sum(np.sum(output))/255
    # area = (usedPixels/(h*w))*100

    # print '\nArea Utilizada: %.2f' % area

    # return output, area
    return develop, develop


def MassCenter(src, area):

    # noise removal Erosion then Dilation
    kernel = np.ones((8, 8), np.uint8)
    area_filtered = cv2.morphologyEx(area, cv2.MORPH_OPEN, kernel, iterations=3)

    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(area_filtered, connectivity=8)

    # print centroids[1:, 0]
    # print stats[0:, 4]
    # print np.dot(centroids[0:, 0], stats[0:, 4])/sum(stats[0:, 4])
    # cm_avX = int(np.dot(centroids[1:, 0], stats[1:, 4])/sum(stats[1:, 4]))
    # cm_avY = int(np.dot(centroids[1:, 1], stats[1:, 4])/sum(stats[1:, 4]))

    cm_avX = int(np.floor(np.average(centroids[1:, 0], weights=stats[1:, 4])))
    cm_avY = int(np.floor(np.average(centroids[1:, 1], weights=stats[1:, 4])))

    print('\nCentro de Masa Total: (' + repr(cm_avX) + ', ' + repr(cm_avY) + ')' )

    for i in range(0, nb_components-1):
        cv2.circle(src, (int(centroids[i+1, 0]), int(centroids[i+1, 1])), 8, (255, 0, 0), -1)

    cv2.circle(src, (cm_avX, cm_avY), 8, (0, 0, 255), -1)

    cv2.namedWindow("CM Total", cv2.WINDOW_NORMAL)
    # im_output = cv2.resize(src, (1080*3, 1080*2))
    cv2.imshow("CM Total", src)


    return (cm_avX, cm_avY)

def DFT2D(src1, src2):

    src1_DFT = np.fft.fft2(src1[0:])
    src1_DFT_shift = np.fft.fftshift(src1_DFT)
    src1_DFT_magnitud = 20 * np.log(np.abs(src1_DFT_shift))

    src2_DFT = np.fft.fft2(src2)
    src2_DFT_shift = np.fft.fftshift(src2_DFT)
    src2_DFT_magnitud = 20 * np.log(np.abs(src2_DFT_shift))

    plt.subplot(221), plt.imshow(src1, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(src1_DFT_magnitud, cmap='jet')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.subplot(223), plt.imshow(src2, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(src2_DFT_magnitud, cmap='jet')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.show()

    # src2_DFT = np.abs(np.fft.fft2(src2))


    return 0


