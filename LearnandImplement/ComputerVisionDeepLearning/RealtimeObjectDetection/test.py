# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:22:39 2021

@author: SP
"""

import cv2
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i",required=True,help="path to image",dest="bar")
args=vars(ap.parse_args())
print(args["bar"])
image=cv2.imread(args["bar"])
image=cv2.resize(image,(500,500))
cv2.imshow("frame",image)
cv2.waitKey(0)
cv2.destroyWindow("frame")
while True:
    image1=cv2.imread(args["bar"])
    image1=cv2.resize(image1,(500,500))
    cv2.imshow("frame1",image1)
    k = cv2.waitKey(1)
    if(k == ord('q')):
        break
cv2.destroyWindow("frame1")
cv2.destroyAllWindows()