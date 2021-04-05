import cv2
import time
import numpy as np


cap = cv2.VideoCapture(0)
# Try using 1 if 0 is not working


while True:
    success, img = cap.read()
    cv2.imshow("Img", img)
    cv2.waitKey(1)
