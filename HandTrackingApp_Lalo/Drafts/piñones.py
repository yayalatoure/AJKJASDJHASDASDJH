import numpy as np
import cv2


import time


cursX = 90
cursY = 90
newX = 90
newY = 90
SupIzqA = 0
SupIzqB = 0
InfDerA = 0
InfDerB = 0

cap = cv2.VideoCapture(0)

def mouseinframe(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        global cursX
        global cursY
        cursY = int(y)
        cursX = int(x)



while True:
    ret, frame = cap.read()

    cv2.imshow('webcam', frame)

    cv2.setMouseCallback('webcam', mouseinframe)

    print (str(cursX) + ' ' + str(cursY))

    k = cv2.waitKey(30) & 0xFF
    if k == 32:
        break

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()