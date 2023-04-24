import sys
import numpy as np
import cv2

src = cv2.imread('namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400
srcQuad = np.zeros((4, 2), dtype=np.float32)
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], dtype=np.float32)
idx = 0

# 마우스 클릭 이벤트 처리 함수


def onMouse(event, x, y, flags, param):
    global idx, srcQuad
    if event == cv2.EVENT_LBUTTONDOWN:
        if idx < 4:
            srcQuad[idx] = [x, y]
            idx += 1
            cv2.circle(dst2, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow('dst2', dst2)
            if idx == 4:
                pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
                dst = cv2.warpPerspective(src, pers, (w, h))
                cv2.imshow('dst', dst)


##cv2.imshow('src', src)
dst2 = src.copy()
cv2.imshow('dst2', dst2)
cv2.setMouseCallback('dst2', onMouse)
cv2.waitKey()
cv2.destroyAllWindows()
