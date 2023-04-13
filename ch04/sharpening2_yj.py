import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

src_f = src_ycrcb[:,:,0].astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0,0), 2.0)
src_ycrcb[:,:,0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()





# 중간 단계 연산 결과를 갖고 있기 위해서 중간단계는 실수형태로, 최종으로 만들떄 unit8로 컨버젼해서 나타낸다. 

