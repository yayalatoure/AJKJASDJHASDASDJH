import pyautogui, sys
from time import sleep
import serial
import math
import time
import cv2
import numpy as np
ser = serial.Serial('COM3',9600)
cap = cv2.VideoCapture(1)
cursX = 90
cursY = 90 
uchar *p = cursX
newX = 90 
newY = 90
SupIzqA = 0
SupIzqB = 0
InfDerA = 0
InfDerB = 0

def mouseinframe(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        cursX = int(x)
        cursY = int(y)
        p = int(x)
        print (str(cursX) + ' ' + str(cursY))
        # return cursX, cursY
   
ret, frame = cap.read()
height, width = frame.shape[:2]
print ('Dimensiones webcam // alto: ' + str(height) + ' ancho: ' + str(width))



print('Apuntar a esquina superior izquierda: ')
while time.time() < t_end:
    ret, frame = cap.read()
    cv2.imshow('webcam',frame)    
    k = cv2.waitKey(30) & 0xFF
    if k == 32:
        break
    cv2.setMouseCallback('webcam',mouseinframe)

    print (str(cursX) + ' ' + str(cursY))
    print (str(newX) + ' ' + str(newY))

    if (cursX != newX or cursY != newY):
        print('culiao')
        xx = int (round(cursX / width * 180))
        yy = 180- int (round(cursY / height * 180))
        xxx = bytes(str(xx),"ascii")
        yyy = bytes(str(yy),"ascii")
        lenX = len(str(xx))
        lenY = len(str(yy))
        newX = cursX
        newY = cursY
        #ser.write ((b'0'*(3-lenX)) +xxx + (b'0'*(3-lenY)) + yyy +b'\n')
        SupIzqA = xx
        SupIzqB = yy
print(SupIzqA)
print(SupIzqB)

print('Apuntar a esquina inferior derecha: ')
while time.time() < (t_end1):
    ret, frame = cap.read()
    cv2.imshow('webcam',frame)    
    k = cv2.waitKey(30) & 0xFF
    if k == 32:
        break
    cv2.setMouseCallback('webcam',mouseinframe)
    if (cursX != newX or cursY != newY):
        xx = int (round(cursX / width * 180))
        yy = 180- int (round(cursY / height * 180))
        xxx = bytes(str(xx),"ascii")
        yyy = bytes(str(yy),"ascii")
        lenX = len(str(xx))
        lenY = len(str(yy))
        newX = cursX
        newY = cursY
        #ser.write ((b'0'*(3-lenX)) +xxx + (b'0'*(3-lenY)) + yyy +b'\n')
        InfDerA = xx
        InfDerB = yy
print(InfDerA)
print(InfDerB)

print ("Calibración terminada")
print('Presiona Ctrl-C para salir')

try:
    while True:
        ret, frame = cap.read()
        cv2.imshow('webcam',frame)    
        k = cv2.waitKey(30) & 0xFF
        if k == 32:
            break
        if (cursX != newX or cursY != newY):
            xx = int (round(SupIzqA + ((cursX / width)*(InfDerA-SupIzqA))))
            yy = SupIzqB - int (round((cursY / height)*(SupIzqB-InfDerB)))
            xxx = bytes(str(xx),"ascii")
            yyy = bytes(str(yy),"ascii")
            lenX = len(str(xx))
            lenY = len(str(yy))
            newX = cursX
            newY = cursY
            #ser.write ((b'0'*(3-lenX)) +xxx + (b'0'*(3-lenY)) + yyy +b'\n')

except KeyboardInterrupt:
    print('\n')
    cap.release()
    cv2.waitKey()
    cv2.destroyAllWindows()