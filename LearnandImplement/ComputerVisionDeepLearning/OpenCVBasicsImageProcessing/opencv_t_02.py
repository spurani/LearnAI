# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:27:27 2021

@author: SP
"""
import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to input image",required=True)
args = vars(ap.parse_args())
print(args)
image = cv2.imread(args["image"])
cv2.imshow("Image",image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY",gray)
cv2.waitKey(0)
edged = cv2.Canny(gray,30,150)
cv2.imshow("Edged",edged)
cv2.waitKey(0)
threshold = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thrash",threshold)
cv2.waitKey(0)
counts = cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
counts =imutils.grab_contours(counts)
output = image.copy()

for i in counts:
    cv2.drawContours(output, [i], -1, (255,0,0), 3)
    cv2.imshow("Contours",output)
    cv2.waitKey(0)
cv2.drawContours(output, counts, -1, (255,0,0), 3)
cv2.imshow("Contours",output)
cv2.waitKey(0)
text = "I found {} objects!".format(len(counts))
cv2.putText(output,text,(10,25),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
cv2.imshow("Contours",output)
cv2.waitKey(0)
mask=threshold.copy()
mask=cv2.erode(mask,None,iterations=5)
cv2.imshow("Erosion",mask)
cv2.waitKey(0)

d = cv2.dilate(threshold.copy(),None,iterations=5)
cv2.imshow("Dilated",d)
cv2.waitKey(0)

m=threshold.copy()
im=cv2.bitwise_and(image,image,mask=m)
cv2.imshow("Masks",im)
cv2.waitKey(0)