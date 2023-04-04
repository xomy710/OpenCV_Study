import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


alpha = 1.0
alpha2 = 2.0

drt = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)
drt2 = np.clip((1 + alpha2) * src - 128 * alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('drt', drt)
cv2.imshow('drt2', drt2)
cv2.waitKey()

cv2.destroyAllWindows()