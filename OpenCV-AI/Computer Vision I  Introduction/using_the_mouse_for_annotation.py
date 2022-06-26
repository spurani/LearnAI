# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:26:25 2021

@author: SP
"""
import cv2

def drawRectangle(action, x, y, flags, userdata):
  # Referencing global variables 
  global ix, iy
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
      ix = x
      iy = y
      cv2.circle(source,(ix,iy),1,(0,255,0),2,cv2.LINE_AA)
  # Action to be taken when left mouse button is released
  if action==cv2.EVENT_LBUTTONUP:
    cv2.rectangle(source, (ix,iy), (x,y), (0,255,0),2,cv2.LINE_AA)
    s=source[iy:y,ix:x]
    cv2.imwrite("f22raptor_cropped.jpg",s)

source = cv2.imread("C:/Users/SP.000/Pictures/Saved Pictures/f22raptor.jpg",cv2.IMREAD_COLOR)
source = cv2.resize(source,(500,500))
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRectangle)
k = 0
# loop until escape character is pressed
while k!=27 :

    cv2.imshow("Window", source)
    cv2.putText(source,'''Choose topleft, and drag, Press ESC to exit''' , (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 2 );
    k = cv2.waitKey(20) & 0xFF

cv2.destroyAllWindows()