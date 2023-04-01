import sys
import cv2


cap = cv2.VideoCapture('video1.mp4')
# cap.open(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
print(w,h)

if not cap.isOpened():
    print('camera open failed!')
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #
    edge = cv2.Canny(frame, 50, 150)
    inversed = ~frame

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('inversed', inversed)
    if cv2.waitKey(20) == 27: #ESC
        break

cap.release()
cv2.destroyAllWindows