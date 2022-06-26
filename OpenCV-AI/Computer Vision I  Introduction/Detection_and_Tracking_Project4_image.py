# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 12:37:20 2021

@author: SP
"""

import cv2
import cv2.dnn as dnn
import numpy as np
def getoutputdetails(outputs):
    boxes = []
    confidences = []
    classIDs = []
    h, w = im.shape[:2]
    for output in outputs:
        for detection in output:
            scores=detection[5:]
            classID=np.argmax(scores)
            confidence=scores[classID]
            if(confidence > 0.5):
                bbox = detection[:4] * np.array([w,h,w,h])
                (centerX,centerY,width,height)=bbox.astype('int')
                x=int(centerX - (width/2))
                y=int(centerY - (height/2))
                box=[x,y,int(width),int(height)]
                boxes.append(box)
                confidences.append(float(confidence))
                classIDs.append(classID)
    return(boxes,confidences,classIDs)

net=dnn.readNet("yolov3.cfg","yolov3.weights")
unconoutlayernames=net.getUnconnectedOutLayersNames()
im = cv2.imread("billboard.jpg")
blob=dnn.blobFromImage(im,1/255.0,(416, 416), (0,0,0), True, False)
net.setInput(blob)
outBlob=net.forward(unconoutlayernames)
(boxes,confidences,classIDs)=getoutputdetails(outBlob)
indices = dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
classes= []
with open("C:/Users/SP.000/Documents/OpenCV AI/coco.txt") as file:
    classes = file.read().strip().split("\n")

print(classes)
print(indices.flatten())
if len(indices) > 0:
    for i in indices.flatten():
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])
        cv2.rectangle(im, (x, y), (x + w, y + h), (255,0,255), 2)
        text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
        cv2.putText(im, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 1)

cv2.imshow("image",im)
waitkey = cv2.waitKey(0)
if (ord('q') == waitkey):
    cv2.destroyAllWindows()
