# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:02:41 2021

@author: SP
"""

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
ap.add_argument("-p","--prototxt",required=True,help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m","--model",required=True,help="path to Caffe pre-trained model")
ap.add_argument("-c","--confidence",type=float,default=0.5,help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
'''Load model from disk'''
print("load the model from your local drive")
print(args["prototxt"])
print(args["model"])
net = cv2.dnn.readNet(args["prototxt"],args["model"])
#Load the input image and construct an input blob for the image
'''The reason for resizing the image to 300x300 is becuase our pretrained model was 
originally trained on 300x300 input_shape'''
image = cv2.imread(args["image"])
(h,w) = image.shape[:2]
### here the last parameter (104.0, 177.0, 123.0) refers to RGB values respectively
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 1.0, (300,300), (104.0, 177.0, 123.0))
print("Detections and Predictions")
net.setInput(blob)
detections = net.forward()
for i in range(0,detections.shape[2]):
    conf=detections[0,0,i,2]
    if(conf > 0.5):
        (startX,startY,endX,endY) = (detections[0,0,i,3:7] * np.array([w, h, w, h])).astype('int') 
        text = '{:.2f}%'.format(conf * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(image, (startX, startY), (endX, endY),(0, 0, 255), 2) 
        cv2.putText(image, text, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)