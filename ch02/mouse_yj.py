import sys
import numpy as np
import cv2

oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: {}, {}'.format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: {}, {}'.format(x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            # print('EVENT_MOUSEMOVE: {}, {}'.format(x, y))
            # cv2.circle(img, (x,y), 5, (0,0,255), -1)
            cv2.line(img, (oldx, oldy), (x,y), (0,0,255), 5, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y



img = np.ones((480, 640, 3), dtype=np.uint8) * 255

# cv2.namedWindow('image')
cv2.imshow('image', img)

cv2.setMouseCallback('image', on_mouse )

cv2.waitKey()

cv2.destroyAllWindows