import cv2
import numpy as np

img = cv2.imread('./imgs/detection_color.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

low_color = np.array([249, 249, 249])
up_color = np.array([255, 255, 255])

mask = cv2.inRange(hsv, low_color, up_color)

cv2.imshow('image', img)
cv2.imshow('mask', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()