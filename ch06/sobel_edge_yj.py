import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

mag = cv2.magnitude(dx,dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

edge = np.zeros(mag.shape[:2], np.uint8)
edge[mag > 125] = 255

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('edge', edge)

cv2.waitKey()

cv2.destroyAllWindows()
