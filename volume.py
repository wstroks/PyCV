import cv2
import numpy as np
import math
from subprocess import call

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    # taking an image
    _, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # get hand data from the rectangle sub window on the screen
    cv2.rectangle(img, (300, 305), (100, 100), (0, 255, 0), 0)
    crop_img = img[100:300, 100:305]
    # convert to grayscale
  # grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    # applying gaussian blur









    cv2.imshow('Gesture', img)
    #all_img = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', crop_img)
    k = cv2.waitKey(10)
    if k == 27:
        break