# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 05:48:20 2021

@author: SP
"""

import cv2
import numpy as np
pts_src_list = []
def onMouseCallback(event,x,y,flags,param):
    pts_src = np.array([])
    if(np.size(pts_src_list,axis=0) != 4):
        if(event == cv2.EVENT_LBUTTONUP):
            pts_src_list.append([x,y])
            pts_src=np.array(pts_src_list)
            cv2.circle(image,(x,y),2,(100,0,255),3,cv2.LINE_AA)
            cv2.imshow("book2",image)
            #return pts_src
        if(np.size(pts_src_list,axis=0) == 4):
            pts_dst=np.array([[0,0],[299,0],[299,399],[0,399]])
            print(pts_dst.shape)
            print(pts_src.shape)
            M,status=cv2.findHomography(pts_src,pts_dst)
            fresh_im=cv2.imread("book2.jpg")
            warp=cv2.warpPerspective(fresh_im,M,(300,400))
            cv2.imshow("Warp Prespective",warp)
image=cv2.imread("book2.jpg")
cv2.namedWindow("book2")
cv2.setMouseCallback("book2",onMouseCallback)
cv2.imshow("book2",image)
waitKey=cv2.waitKey(0) & 0xFF
if(waitKey == ord('q') or waitKey == ord('Q') or waitKey == 27):
    cv2.destroyAllWindows()