import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

'''
kernel = np.array([
                    [-1, 0, 1],
                    [-2, 0 ,2], 
                    [-1, 0, 1]], dtype=np.float32)

dx = cv2.filter2D(src, -1, kernel, delta=128)
'''

dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)


cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
