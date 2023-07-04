import cv2
import dlib
import numpy as np


def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the image using OpenCV
image = cv2.imread("Man2.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
rects = detector(gray, 1)

for (i, rect) in enumerate(rects):
    shape = predictor(gray, rect)
    shape = shape_to_np(shape)

    # Write the detected facial landmarks to a .txt file
    with open('image.txt', 'w') as file:
        for (x, y) in shape:
            file.write(str(x) + ' ' + str(y) + '\n')

print("Facial landmarks for the detected faces have been written to 'image.txt'")
