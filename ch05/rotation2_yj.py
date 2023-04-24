import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


angle = 0;

cp = (src.shape[1] / 2, src.shape[0] / 2)


while True:
    
    rot = cv2.getRotationMatrix2D(cp, angle, 0.5)
    dst = cv2.warpAffine(src, rot, (0, 0))
    
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(' '):
        angle += 10
        if angle == 360:
            angle = 0



cv2.destroyAllWindows()