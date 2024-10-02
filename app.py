import cv2
import numpy as np
from pyzbar.pyzbar import decode
# for barcode detection

# img = cv2.imread('barcode.png') --> commenting out for webcam
# decoder = decode(img)
# for webcam
cap = cv2.VideoCapture(0)  # O is the default camera, 1 is outside camera,2,3,...
cap.set(3, 640)  # width id = 3, width dim of webcam
cap.set(4, 480)  # height id = 4, height dim of webcam

while True:
    success, img = cap.read()
    for barcode in decode(img):
        print(barcode.data)  # barcode data
        # print(barcode.type) #barcode type, e.g. QRCODE
        # print(barcode.rect) #position and size of barcode boundary box
        myData = barcode.data.decode('utf-8')  # string converter
        print(myData)
        # bounding box (polygon)
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(img, [points], True, (255, 0, 255), 5)
        # to print message
        points2 = barcode.rect
        cv2.putText(img, myData, (points2[0], points2[1]), cv2.FONT_HERSHEY_SIMPLEX
                    , 0.9, (255, 0, 255), 3)
    cv2.imshow('Result', img)
    cv2.waitKey(1) # 1-millisecond window wait time




