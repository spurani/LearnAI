# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:50:52 2021

@author: SP
"""

import cv2
import numpy as np
videoCap=cv2.VideoCapture(0)
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Trackbar controllers")
def nothing(x):
    pass
cv2.createTrackbar("L-H","Trackbar controllers",0,179,nothing)
cv2.createTrackbar("U-H","Trackbar controllers",179,179,nothing)
cv2.createTrackbar("L-S","Trackbar controllers",0,254,nothing)
cv2.createTrackbar("U-S","Trackbar controllers",254,254,nothing)
cv2.createTrackbar("L-V","Trackbar controllers",0,254,nothing)
cv2.createTrackbar("U-V","Trackbar controllers",254,254,nothing)
while (videoCap.isOpened()):
    ret,frame=videoCap.read()
    if(ret== True):
        hsvframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        UH=cv2.getTrackbarPos("U-H","Trackbar controllers")
        US=cv2.getTrackbarPos("U-S","Trackbar controllers")
        UV=cv2.getTrackbarPos("U-V","Trackbar controllers")
        LH=cv2.getTrackbarPos("L-H","Trackbar controllers")
        LS=cv2.getTrackbarPos("L-S","Trackbar controllers")
        LV=cv2.getTrackbarPos("L-V","Trackbar controllers")
        lowercolour=np.array([LH,LS,LV])
        uppercolour=np.array([UH,US,UV])
        mask=cv2.inRange(hsvframe,lowercolour,uppercolour)
        mask=cv2.bitwise_and(mask,mask,cv2.THRESH_BINARY_INV)
        cv2.imshow("MASK",mask)
        cv2.imshow("Frame",frame)
        cv2.imshow("Trackbar controllers",img)
        waitkey=cv2.waitKey(1) & 0xFF
        if(ord('q') == waitkey or ord('Q') == waitkey):
            break
    else:
        break

videoCap.release()
cv2.destroyAllWindows()