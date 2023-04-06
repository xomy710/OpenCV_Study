
import cv2
import numpy as np
import sys

List1 = [0, 256]
List2 = [0, 256]

List_Final = List1 + List2

print(List_Final)


# 입력 영상에서 ROI를 지정하고, 히스토그램 계산

src = cv2.imread('cropland.png')

if src is None:
    print('Image load failed!')
    sys.exit()

x, y, w, h = cv2.selectROI(src)

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
crop = src_ycrcb[y:y+h, x:x+w]

print([crop])
#crop과 [crop]의 차이가 있을까? 테스트해볼예쩡