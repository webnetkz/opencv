import cv2
import numpy as np
from mss.windows import MSS as mss

import time

img = cv2.imread('./imgs/detection_color.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

low_color = np.array([204, 78, 73])
up_color = np.array([204, 78, 73])

with mss() as sct:
    monitor = {"top": 40, "left": 0, "width": 800, "height": 640}

    while "Screen capturing":
        last_time = time.time()
        img = np.array(sct.grab(monitor))
        cv2.imshow("OpenCV/Numpy normal", img)
        print("fps: {}".format(1/(time.time() - last_time)))

        color_yellow = (0,255,255)

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        thresh = cv2.inRange(hsv, low_color, up_color)

        moments = cv2.moments(thresh, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']

        if dArea > 100:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv2.circle(img, (x, y), 10, (0,0,255), -1)
            cv2.circle(img, (x, y), 5, color_yellow, 2)

            print("123")

        cv2.imshow('result', img)
        ch = cv2.waitKey(5)
        if ch == 27:
            break

    cv2.destroyAllWindows()

