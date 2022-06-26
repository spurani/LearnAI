# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 18:01:29 2021

@author: SP
"""

import cv2

def scroll_resizer_Mouse_Callback(event, x, y, flag, userdata):
    if((event == cv2.EVENT_MOUSEWHEEL) and (flag & event == cv2.EVENT_FLAG_CTRLKEY)):
        if(flag > 0):
            print(x,y)
            print(event)
            print(flag)

image = cv2.imread("C:/Users/SP.000/Pictures/Saved Pictures/f22raptor.jpg")
image = cv2.resize(image,(500,500))
cv2.namedWindow("f22raptor")
cv2.setMouseCallback("f22raptor", scroll_resizer_Mouse_Callback)
cv2.imshow("f22raptor",image)
k = cv2.waitKey(0)
if(k == ord('q') or k == 27):
    cv2.destroyWindow("f22raptor")
    