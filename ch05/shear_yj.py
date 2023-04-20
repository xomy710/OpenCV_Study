import sys
import numpy as np
import cv2

src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0.5 ,0], [0, 1, 0]], dtype=np.float32)

h,w = src.shape[:2]
## 함수에 int사용하는 이유는, 0.5를 곱하면 소수점이 나오는데, warpAffine함수는 정수만 받기 떄문이다. 
dst = cv2.warpAffine(src, aff, ( w + int(h * 0.5) , h ))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

