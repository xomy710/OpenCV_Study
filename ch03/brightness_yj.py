import sys
import numpy as np
import cv2

# src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('lenna.bmp')

dst = cv2.add(src, (100,100,100,0))
# dst = np.clip(src + 100., 0,255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()