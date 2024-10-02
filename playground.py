import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('barcode.png')
code = decode(img)
print(code) # a list

for barcode in code:
    print(barcode.data.decode('utf-8'))
    print(barcode.type)
    print(barcode.polygon)
    points = np.array([barcode.polygon],np.int32)
    print(points)
    # print(points.reshape((-1, 1, 2)))
    print(barcode.rect)
    pts = barcode.rect
    print(pts[0],pts[1])