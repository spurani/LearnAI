# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:46:24 2021

@author: SP
"""

import cv2
scaleFactor=1
maxScaleUp=100
scaleType=0
maxType=1
def scaleImage(val):
    global scaleFactor
    global scaleType
    if (scaleType == 0):
        scaleFactor = 1 + (val / 100)
    if (scaleType == 1):
        scaleFactor = 1 - (val/100)
    if (scaleFactor == 0):
        scaleFactor = 1
    scaled_image=cv2.resize(img,(0,0),fx=scaleFactor,fy=scaleFactor,interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Resize Image",scaled_image)
def scaleTypeImage(val):
    global scaleFactor
    global scaleType
    if (scaleType == 0):
        print("Before: ",scaleFactor)
        #Here we are keeping track of scalefactor which will be used to resetting the image size back based newly selected scaletype
        scaleFactor = 1 + (scaleFactor / 100)
        print("After: ",scaleFactor)
        scaleType = val
    else:
        print("Before: ",scaleFactor)
        #Here we are keeping track of scalefactor which will be used to resetting the image size back based newly selected scaletype
        scaleFactor = 1 - (scaleFactor / 100)
        print("After: ",scaleFactor)
        scaleType = val
    if (scaleFactor == 0):
        scaleFactor = 1
    scaled_image=cv2.resize(img,(0,0),fx=scaleFactor,fy=scaleFactor,interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Resize Image",scaled_image)
Window="Resize Image"
img=cv2.imread("C:/Users/SP.000/Pictures/Saved Pictures/f22raptor.jpg",cv2.IMREAD_COLOR)
img=cv2.resize(img,(500,500))
cv2.namedWindow(Window,cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Scale",Window,scaleFactor,maxScaleUp,scaleImage)
cv2.createTrackbar("Type: \n 0: Scale Up \n 1: Scale Down",Window,scaleType,maxType,scaleTypeImage)
#cv2.imshow(Window,img)
scaleImage(10)
cv2.waitKey()
cv2.destroyAllWindows()