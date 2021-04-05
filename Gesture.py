import cv2
import time
import numpy as np


widcam, htcam = 640, 480


cap = cv2.VideoCapture(0)
# Try using 1 if 0 is not working

cap.set(3, widcam)
cap.set(4, htcam)

# 3 and 4 are  internally set for widcam and htcam

ptime = 0
while True:
    success, img = cap.read()

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, f'FPS:{int(fps)}', (40, 40),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
