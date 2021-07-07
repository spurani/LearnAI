# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:09:24 2021

@author: SP
"""

import cv2
import imutils
import numpy as np
import argparse
from collections import deque
import time
ap = argparse.ArgumentParser()
ap.add_argument('-v',"--video",help="pass video file",required=True)
ap.add_argument('-b',"--buffer",help="buffer video frame",type=int,default=64)
args = vars(ap.parse_args())
lower_green=(29,86,6)
upper_green=(64,255,255)
pts = deque(maxlen=args["buffer"])
print(pts)
vs=cv2.VideoCapture(args["video"])
time.sleep(2.0)
while True:
    frame=vs.read()
    frame = frame[1] if args.get("video", False) else frame    
    if frame is None:
        break
    frame=imutils.resize(frame,width=600)
    blur=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_green,upper_green)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    contours=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(contours)
    center=None
    if(len(contours) > 0):
        largestcontour = max(contours,key=cv2.contourArea)
        ((x,y),radius) = cv2.minEnclosingCircle(largestcontour)
        M = cv2.moments(largestcontour)
        center = int(M["m10"] / M['m00']), int(M['m01'] / M['m00'])
        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,0),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
    pts.appendleft(center)
    print(pts)
    for i in range(1,len(pts)):
        if(pts[i-1] is None or pts[i] is None):
            continue
        thickness = int(np.sqrt(args["buffer"]/float(i+1))*2.5)
        cv2.line(frame,pts[i-1],pts[i],(0,0,255),thickness)
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if(key == 'q'):
        break
vs.release()
cv2.destroyAllWindows()