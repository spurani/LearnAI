# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 21:06:46 2021

@author: SP
"""

import cv2
import numpy as np
import argparse
import sys
import imutils
import transform
from skimage.filters import threshold_local
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Path to input image",required=True)
arg = vars(ap.parse_args())
image = cv2.imread(arg["image"])
resize = imutils.resize(image,height=500)
image = imutils.resize(image,height=500)
orig = image.copy()
ratio = image.shape[0] / 500.0
gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
edge = cv2.Canny(blur, 75, 200)
cnts = cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea,reverse=True)[:5]
for c in cnts:
    pericounts = cv2.arcLength(c,True)
    approxcounts = cv2.approxPolyDP(c,0.02*pericounts,True)
    
    if(len(approxcounts) == 4):
        screenCnt = approxcounts
        break
cv2.drawContours(image,[screenCnt],-1,(255,0,0),2)
w = transform.four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
wbgrgray= cv2.cvtColor(w, cv2.COLOR_BGR2GRAY)
T = threshold_local(wbgrgray, 11, offset = 10, method = "gaussian")
warped = (wbgrgray > T).astype("uint8") * 255
# show the original and scanned images
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)