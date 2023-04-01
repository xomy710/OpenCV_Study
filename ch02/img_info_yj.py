import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

h, w = img1.shape[:2]
print('w x h = {} x {}'.format(w,h))

h, w = img2.shape[:2]
print('w x h = {} x {}'.format(w,h))

#if img1.ndim == 2:
#    print('img1 is a grayscale imgae')

if len(img1.shape) == 2:
    print('img1 is a grayscale imgae')

# x = 20
# y = 10
# p1 = img1[y, x]
# print(p1)

# img1[y, x] = 0 

# p2 = img2[y,x]
# print(p2)

# img2[y, x] = (0, 0, 255) 

# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 0
#         img2[y, x] = (0, 255, 255)

img1[:,:] = 0
img2[:,:] = (0, 255, 255)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()