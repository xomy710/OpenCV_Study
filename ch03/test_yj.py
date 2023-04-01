import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)

img2 = np.zeros((480, 640, 3), np.uint8)

img3 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
img4 = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)

cv2.imshow('image', img1)
cv2.waitKey()
