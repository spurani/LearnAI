# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 11:47:18 2021

@author: SP
"""
import imutils
import cv2

image = cv2.imread("vk_starter.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
cv2.imshow("full",image)
cv2.waitKey(0)
print(image[100,50])
(B, G, R) = image[100,50]
print("R={}, G={}, B={}".format(R,G,B))
roi = image[60:160, 320:420]
cv2.imshow("Image",roi)
cv2.waitKey(0)
resize = cv2.resize(image,(300,300))
cv2.imshow("Resize",resize)
cv2.waitKey(0)
rw = 300.0 / w
dim  = (300, int(h * rw))
resizedaspect = cv2.resize(image, dim)
cv2.imshow("ASpect ratio maintained",resizedaspect)
cv2.waitKey(0)
resizedutils = imutils.resize(image,width=300)
cv2.imshow("Imutils resize",resizedutils)
cv2.waitKey(0)

center = (w // 2, h //2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w,h))
cv2.imshow("Opencv Rotaion", rotated)
cv2.waitKey(0)

imutilsrotate = imutils.rotate(image, -45)
#cv2.imshow("Imutils Rotate",imutilsrotate)
#cv2.waitKey(0)

imutilsrotatebound = imutils.rotate_bound(image, -45)
#cv2.imshow("Imutils Rotate",imutilsrotatebound)
#cv2.waitKey(0)

blurred = cv2.GaussianBlur(image,(15,15),0)
# cv2.imshow("Blurred",blurred)
# cv2.waitKey(0)

recdrawim = image.copy()
#cv2.rectangle(recdrawim,(10,60),(500,160),(0,0,255),2)
#cv2.imshow("Rectangle",recdrawim)
#cv2.waitKey(0)

cv2.putText(recdrawim,"Virat Kohli Early Days",(10,25),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
cv2.imshow("VK text",recdrawim)
cv2.waitKey(0)