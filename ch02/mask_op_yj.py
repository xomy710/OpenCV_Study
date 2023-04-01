import sys
import cv2


# 마스크 영상을 이용한 영상 합성
# src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
# mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

src = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:, :, -1]
src = src[:, :, 0:3]
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]

crop = dst[10:h + 10, 10:w + 10]

cv2.copyTo(src, mask, crop)

# cv2.copyTo(src, mask, dst)

# dst[mask >0] = src[mask>0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
