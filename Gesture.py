import cv2
import time
import numpy as np
import Track as htm

widcam, htcam = 640, 480


cap = cv2.VideoCapture(0)
# Try using 1 if 0 is not working

cap.set(3, widcam)
cap.set(4, htcam)

# 3 and 4 are  internally set for widcam and htcam

ptime = 0

detector = htm.handDetector(detectionCon=0.7)  # detection Confidence


while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, f'FPS:{int(fps)}', (40, 40),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
