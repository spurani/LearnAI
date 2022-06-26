# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 16:28:22 2021

@author: SP
"""

import cv2
k=0
cap=cv2.VideoCapture(0)
if(cap.isOpened()):
    while True:
        if(k == ord('q')):
            break
        ret, frame=cap.read()
        cv2.imshow("frame",frame)
        k=cv2.waitKey(1)
        
    cap.release()
    cv2.destroyAllWindows()
else:
    cap.release()
    