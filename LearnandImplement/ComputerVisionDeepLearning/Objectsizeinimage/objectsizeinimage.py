# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 02:16:27 2021

@author: SP
"""
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours as utilscontours
import numpy as np
import argparse
import imutils
import cv2

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to image")
ap.add_argument("-w","--width",type=float,required=True,help="width of the lef-most object")
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(7,7),0)
edge=cv2.Canny(blur,50,100)
dilate=cv2.dilate(edge,None,iterations=1)
erode=cv2.erode(dilate,None,iterations=1)
contours=cv2.findContours(erode,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(contours)
(contours,_)=utilscontours.sort_contours(contours)
pixelsPerMetric=None
for c in contours:
    if(cv2.contourArea(c) < 100):
        continue
    orig=image.copy()
    box=cv2.minAreaRect(c)
    box=cv2.boxPoints(box)
    box=np.array(box,dtype="int")
    box=perspective.order_points(box)
    cv2.drawContours(orig,[box.astype("int")],-1,(0,255,0),2)
    for(x,y) in box:
        cv2.circle(orig,(int(x),int(y)),5,(0,0,255),-1)
    (tl, tr, br, bl) = box
    (tltrX, tltrY) = midpoint(tl, tr)
    (blbrX, blbrY) = midpoint(bl,br)
    
    (tlblX, tlblY) = midpoint(tl, bl)
    (trbrX, trbrY) = midpoint(tr,br)
    
    cv2.circle(orig,(int(tltrX), int(tltrY)),5,(155,0,0))
    cv2.circle(orig,(int(blbrX), int(blbrY)),5,(155,0,0))
    cv2.circle(orig,(int(tlblX), int(tlblY)),5,(155,0,0))
    cv2.circle(orig,(int(trbrX), int(trbrY)),5,(155,0,0))
    
    cv2.line(orig,(int(tltrX), int(tltrY)),(int(blbrX), int(blbrY)),(255,0,255))
    cv2.line(orig,(int(tlblX), int(tlblY)),(int(trbrX), int(trbrY)),(255,0,255))

    dA= dist.euclidean((tltrX, tltrY),(blbrX, blbrY))
    dB = dist.euclidean((tlblX, tlblY),(trbrX, trbrY))
    if(pixelsPerMetric is None):
        pixelsPerMetirc = dB / args["width"]
    dimA = dA / pixelsPerMetirc
    dimB = dB / pixelsPerMetirc
    cv2.putText(orig, "{:.1f}in".format(dimA),
		(int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
    cv2.putText(orig, "{:.1f}in".format(dimB),
		(int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX,
		0.65, (255, 255, 255), 2)
    cv2.imshow("image",orig)
    cv2.waitKey(0)