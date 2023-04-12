import sys 
import numpy as np
import cv2

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

blr = cv2.GaussianBlur(src, (0,0), 2)

#dst = cv2.subtract(src, blr)

#뺐을 때 코드확인
#dst = cv2.addWeighted(src, 1, blr, -1, 128)

#dst = cv2.addWeighted(src, 2, blr, -1, 0)

dst = np.clip(2.0*src - blr, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()