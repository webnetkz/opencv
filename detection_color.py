import cv2
import numpy as np

img = cv2.imread('./imgs/detect_color.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

up_color = np([])
low_color = np([])

mask = cv2.inRange(img, up_color, low_color)


cv2.waitKey(0)
cv2.destroyAllWindows()