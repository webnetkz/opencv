import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 600)
cap.set(4, 400)

while True:
    success, img = cap.read()

    cv2.imshow("Testing", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break