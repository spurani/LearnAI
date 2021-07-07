# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:07:01 2021

@author: SP
"""

import cv2
import numpy as np
import time
from imutils.video import FPS
from imutils.video import VideoStream
import imutils
import argparse
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
net=cv2.dnn.readNetFromCaffe("deploy.prototxt.txt","MobileNetSSD_deploy.caffemodel")
'''video=VideoStream(0).start()
time.sleep(2.0)
fps = FPS().start()
while True:
    frame1=video.read()
    frame_resized=imutils.resize(frame1,width=400)
    (h, w) = frame_resized.shape[:2]
    blob=cv2.dnn.blobFromImage(cv2.resize(frame_resized, (300, 300)),
		0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections=net.forward()
    for i in range(0,detections.shape[2]):
    #if(detections[6] > 0.5): 
        confidence=detections[0,0,i,2]
        if(confidence>0.5):
            idx=int(detections[0,0,i,1])
            boxes=detections[0,0,i,3:7]*np.array([w,h,w,h])
            (startX,startY,endX,endY) = boxes.astype('int')
            label="{}: {:.2f}".format(CLASSES[idx],confidence)
            print(label)
            cv2.rectangle(frame1,(startX,startY),(endX,endY),COLORS[idx],2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame1,label,(startX,y),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.5,COLORS[idx],2)
    cv2.imshow("frame",frame1)
    key=cv2.waitKey(1) & 0xFF
    if (key == ord("q")):
        break
fps.stop()
cv2.destroyAllWindows()
video.stop()'''
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to image",required=True)
args=vars(ap.parse_args())
image=cv2.imread(args["image"])
image_resize=cv2.resize(image,(500,500))
(w,h) = (image_resize.shape[0],image_resize.shape[1])
print(image_resize.shape)
blob=cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),0.007843, (300, 300), 127.5)
net.setInput(blob)
detections=net.forward()
for (idx,detection) in enumerate(detections):
    confidence=detections[0][0][idx][2]
    classindex=detections[0][0][idx][1]
    if(confidence > 0.5):
        boxes=detections[0][0][idx][3:7]*np.array([w,h,w,h])
        (startX,startY,endX,endY)=boxes.astype('int')
        cv2.rectangle(image_resize,(startX,startY),(endX,endY),COLORS[idx],2)
        print((startX,startY,endX,endY))
    print(detection[0][0])
cv2.imshow("image",image_resize)
cv2.waitKey(0)