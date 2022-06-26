# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:38:39 2022

@author: SP
"""

import cv2
import numpy as np

im=cv2.imread("shapes.jpg")
width=im.shape[0]
height=im.shape[1]
new_width=500
aspect_ratio=new_width/height
size=(new_width,int(aspect_ratio * width))
new_image=cv2.resize(im,size,interpolation=cv2.INTER_AREA)
gray=cv2.cvtColor(new_image,cv2.COLOR_BGR2GRAY)
cv2.imshow("image",gray)
_,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)
cv2.imshow("threshold",thresh)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
imagecopy=new_image.copy()
drawcontours=cv2.drawContours(imagecopy,contours,-1,(255,0,255),3,cv2.LINE_8)
cv2.imshow("Contours",drawcontours)
n_3=new_image.copy()
drawcontours_3=cv2.drawContours(n_3,contours,3,(255,0,255),3,cv2.LINE_8)
cv2.imshow("Contour 3",drawcontours_3)

for cnt in contours:
    M = cv2.moments(cnt)
    x = int(round(M["m10"]/M["m00"]))
    y = int(round(M["m01"]/M["m00"]))
    cv2.circle(drawcontours,(x,y),5,(255,0,0),-1)
cv2.imshow("Centroid or Center of Mass",drawcontours)

for idx,cnt in enumerate(contours):
    area=cv2.contourArea(cnt)
    perimeter=cv2.arcLength(cnt,True)
    print("Contour #{} has area = {} and perimeter = {} ".format(idx+1,area,perimeter))

n_5=new_image.copy()
for cnt in contours:
    x,y,w,h=cv2.boundingRect(cnt)
    cv2.rectangle(n_5,(x,y),(x+w,y+h),(0,255,0),1)
cv2.imshow("Bounding Rectangle",n_5)

n_6=new_image.copy()
for cnt in contours:
    box=cv2.minAreaRect(cnt)
    boxPts=np.int0(cv2.boxPoints(box))
    cv2.drawContours(n_6,[boxPts],-1,(0,255,0),2)
cv2.imshow("MinArea Rectangle",n_6)

n_7=new_image.copy()
for cnt in contours:
    ((x,y),radius) = cv2.minEnclosingCircle(cnt)
    cv2.circle(n_7,(int(x),int(y)),int(round(radius)),(0,255,0),3)
cv2.imshow("MinEnclosing Circle",n_7)

key=cv2.waitKey(0)
if(key):
    cv2.destroyAllWindows()
