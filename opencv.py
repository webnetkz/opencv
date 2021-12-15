import numpy as np
import cv2

cap = cv2.VideoCapture(0)
lower_color = np.array([211, 212, 201])
upper_color = np.array([235, 237, 234])

while True: 
    
    ret,img=cap.read()

    rgb = cv2.cvtColor(cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(img, lower_color, upper_color)

    
    cv2.imshow('Video', img)
    
    if(cv2.waitKey(10) & 0xFF == ord('b')):
        break

