import numpy as np
import cv2


def on_trackbar(pos):
    global img

    level = pos * 16
    # if level >= 255:
    #     level = 255
    level = np.clip(level, 0, 255)

    img[:, :] = level
    cv2.imshow('image_yj', img)
    # print(pos)

img = np.zeros((480,640), np.uint8)

cv2.namedWindow('image_yj')
cv2.imshow('image_yj', img)

cv2.createTrackbar('level', 'image_yj', 0, 16, on_trackbar)

cv2.waitKey()

cv2.destroyAllWindows()