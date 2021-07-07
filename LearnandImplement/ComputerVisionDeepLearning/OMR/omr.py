# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 05:06:46 2021

@author: SP
"""

import cv2
import imutils
from imutils import contours
import transform
import argparse
import transform
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help="Image input path")
ag = vars(ap.parse_args())
image = cv2.imread(ag["image"])
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(blur,75,200)
cnts = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# print(cnts)
if(len(cnts) > 1):
    cnts = sorted(cnts,key=cv2.contourArea,reverse=True)
# print("_______--------------________")
# print(cnts)
# print("_______--------------________")
finalcnts = None
for i in cnts:
    peri = 0.1*cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,peri,True)
    # print(approx)
    if(len(approx) == 4):
        finalcnts = approx
cv2.drawContours(image,[finalcnts],-1,(255,0,0),3)
cv2.drawContours(gray,[finalcnts],-1,(255,0,0),3)
#cv2.imshow("image",image)
paperimage = transform.four_point_transform(image,finalcnts.reshape(4,2))
warpedimage = transform.four_point_transform(gray,finalcnts.reshape(4,2))
#cv2.imshow("paperimage",paperimage)
#cv2.imshow("warpedimage",warpedimage)
thresh=cv2.threshold(warpedimage,0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
threshcnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow("thresh",thresh)
threshcnts = imutils.grab_contours(threshcnts)
questioncnts = []
for j in threshcnts:
    (x,y,w,h) = cv2.boundingRect(j)
    ar = w/float(h)
    if(w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1):
        questioncnts.append(j)
        #cv2.drawContours(paperimage,[j],-1,(0,255,0),3)
        #cv2.imshow("questionandpaper",paperimage)
#print(questioncnts)
qCnts = contours.sort_contours(questioncnts,method="top-to-bottom")[0]
right=0
print(qCnts)
for (q, i) in enumerate(np.arange(0, len(qCnts), 5)):
    cnts = contours.sort_contours(qCnts[i:i + 5])[0]
    bubbled = None
    for (j, c) in enumerate(cnts):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            mask = cv2.bitwise_and(thresh, thresh, mask=mask)
            total = cv2.countNonZero(mask)
            if bubbled is None or total > bubbled[0]:
                bubbled = (total, j) 
            color = (0, 0, 255)
            k = ANSWER_KEY[q]
            if k == bubbled[1]:
        	    color = (0, 255, 0)
        	    right += 1
            cv2.drawContours(paperimage, [cnts[k]], -1, color, 3)
score = (right / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paperimage, "{:.2f}%".format(score), (10, 30),
	cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", paperimage)
cv2.waitKey(0)