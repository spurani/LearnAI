# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:05:26 2021

@author: SP
"""

import cv2
import numpy as np
from scipy.spatial import distance as dist
def reorder_coordinates_points(points):
	xSorted = points[np.argsort(points[:, 0]), :]
	leftMost = xSorted[:2, :]
	rightMost = xSorted[2:, :]
	leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
	(tl, bl) = leftMost
	D = dist.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
	(br, tr) = rightMost[np.argsort(D)[::-1], :]
	return np.array([tl, tr, br, bl], dtype="float32")

def get_WxH_repectively(image, points):
    rect = reorder_coordinates_points(points)
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    return maxWidth,maxHeight,rect

pts_dst_list = []
def onMouseCallback(event,x,y,flags,param):
    pts_dst = np.array([])
    if(np.size(pts_dst_list,axis=0) != 4):
        if(event == cv2.EVENT_LBUTTONUP):
            pts_dst_list.append([x,y])
            pts_dst=np.array(pts_dst_list)
            cv2.circle(image,(x,y),2,(100,0,255),3,cv2.LINE_AA)
            cv2.imshow("billboard",image)
        if(np.size(pts_dst_list,axis=0) == 4):
            w,h,rect=get_WxH_repectively(image,pts_dst)
            (tl, tr, br, bl) = rect
            print("tl: ",tl," tr: ",tr," br: ",br," bl: ",bl)
            pts_src=np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]])
            M,status=cv2.findHomography(pts_src,pts_dst)
            fresh_im=cv2.imread("first-image.jpg")
            fresh_image_resize=cv2.resize(fresh_im,(w,h))
            cv2.imshow("resizer",fresh_image_resize)
            warp=cv2.warpPerspective(fresh_image_resize,M,(image.shape[1],image.shape[0]))
            cv2.imshow("Warp Prespective",warp)
            im_c=image.copy()
            mask = cv2.fillPoly(im_c,[pts_dst],(0,0,0),cv2.LINE_AA)
            cv2.imshow("masked_cropped",mask)
            ander=cv2.bitwise_or(warp,mask)
            cv2.imshow("ander",ander)
image=cv2.imread("billboard.jpg")
cv2.namedWindow("billboard")
cv2.imshow("billboard",image)
cv2.setMouseCallback("billboard",onMouseCallback)
waitKey=cv2.waitKey(0) & 0xFF
if(waitKey == ord('q') or waitKey == ord('Q') or waitKey == 27):
    cv2.destroyAllWindows()