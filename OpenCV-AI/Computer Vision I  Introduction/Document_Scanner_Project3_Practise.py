# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 11:03:17 2021

@author: SP
"""

import cv2
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
def MouseCallback(event,x,y,flags,userdata):
    global startx,starty, ori_img, ori_img2, is_drawing, is_rect_drawn, width, height
    if((event == cv2.EVENT_RBUTTONDOWN) and (flags == cv2.EVENT_FLAG_RBUTTON)):
        is_drawing = True
        startx = x
        starty = y
    elif((event == cv2.EVENT_MOUSEMOVE) and (flags == cv2.EVENT_FLAG_RBUTTON)):
        if(is_drawing == True and is_rect_drawn == False):
            ori_img=ori_img2.copy()
            cv2.rectangle(ori_img,(startx,starty),(x,y),(0,255,255),2,cv2.LINE_AA)
    elif(event == cv2.EVENT_RBUTTONUP):
        if(is_drawing == True and is_rect_drawn == False):
            ori_img=ori_img2.copy()
            cv2.rectangle(ori_img,(startx,starty),(x,y),(0,255,255),2,cv2.LINE_AA)
            cv2.putText(ori_img,"PRESS 0 to Scan",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1,cv2.LINE_AA)
            is_drawing=False
            is_rect_drawn=True
            img3=ori_img2.copy()
            img3=img3[starty:y,startx:x]
            width=(x-startx)
            height=(y-starty)
ori_img=cv2.imread("scanned-form.jpg")
w=500
aspectratio=w/ori_img.shape[1]
dim=(500,int(aspectratio*ori_img.shape[0]))
ori_img=cv2.resize(ori_img,dim)
ori_img2=ori_img.copy()
bdgModel=np.zeros((1,65),dtype=np.float64)
fdgModel=np.zeros((1,65),dtype=np.float64)
mask=np.zeros(ori_img.shape[:2],dtype=np.uint8)
startx=0
starty=0
applycontours=False
is_drawing=False
is_rect_drawn=False
cv2.namedWindow("Original Image")
cv2.setMouseCallback("Original Image",MouseCallback)
print("INSTRUCTIONS")
print("DRAW a rectangle around the document to scan and Press 0")
while(True):
    cv2.putText(ori_img,"PRESS Q to Quit",(300,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1,cv2.LINE_AA)
    cv2.imshow("Original Image", ori_img)
    waitKey=cv2.waitKey(1) & 0xFF
    if (waitKey == ord('q')):
        break
    if(waitKey == ord('0')):
        rect=(startx,starty,width,height)
        cv2.grabCut(ori_img2,mask,rect,bdgModel,fdgModel,1,cv2.GC_INIT_WITH_RECT)
        applycontours = True
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = ori_img*mask2[:,:,np.newaxis]
    if(applycontours == True):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(gray, 152, 255, cv2.THRESH_BINARY)
        contours,heirarchy = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for i in contours:
            epsilon = 0.1*cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,epsilon,True)
            cv2.drawContours(img,approx,-1,(0,255,0),4)    
        applycontours=False
        dst=np.array([
            [0,0],
            [width,0],
            [width,height],
            [0,height]
            ])
        if(len(approx) == 4):  
            new_approx=np.empty((4,2),int)
            for idx,value in enumerate(approx):
                new_approx[idx]=value[0]
            s = new_approx.sum(axis = 1)
            rect = np.zeros((4, 2), dtype = "float32")
            rect[0] = new_approx[np.argmin(s)]
            rect[2] = new_approx[np.argmax(s)]
            diff = np.diff(new_approx, axis = 1)
            rect[1] = new_approx[np.argmin(diff)]
            rect[3] = new_approx[np.argmax(diff)]
            h, status=cv2.findHomography(rect,dst)
            wrapped=cv2.warpPerspective(img,h,(width,height))
            cv2.imshow("wrapped",wrapped)
            cv2.imshow("new img",img)
    cv2.imshow("Output",img)
cv2.destroyAllWindows()