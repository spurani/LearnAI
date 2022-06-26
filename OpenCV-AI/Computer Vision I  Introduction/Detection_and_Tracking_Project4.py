# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 08:48:28 2021

@author: SP
"""

import cv2
import cv2.dnn as dnn
import numpy as np

def getoutputdetails(outputs):
    boxes = []
    confidences = []
    classIDs = []
    h, w = video.shape[:2]
    for output in outputs:
        for detection in output:
            scores=detection[5:]
            classID=np.argmax(scores)
            if(classID == 32):
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
    return (boxes,confidences,classIDs)

def getdetectionsfromnetwork():
    blob=dnn.blobFromImage(video,1/255.0,(416, 416), (0,0,0), True, False)
    net.setInput(blob)
    outBlob=net.forward(unconoutlayernames)
    (boxes,confidences,classIDs)=getoutputdetails(outBlob)
    indices = dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    return (boxes,confidences,classIDs,indices)

def detectionrectangle(boxes,confidences,classIDs,indices):
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            cv2.rectangle(video, (x, y), (x + w, y + h), (0,255,0), 2)
            bbox = (x, y,x + w, y + h)
            global tracker
            tracker = cv2.TrackerKCF_create()
            tracker.init(video,bbox)
            text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
            cv2.putText(video, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 1)

net=dnn.readNet("yolov3.cfg","yolov3.weights")
unconoutlayernames=net.getUnconnectedOutLayersNames()
cap = cv2.VideoCapture("soccer-ball.mp4")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
cap_writer = cv2.VideoWriter('filename.avi',cv2.VideoWriter_fourcc(*'MJPG'),25,size)
classes= []
counter=0
with open("C:/Users/SP.000/Documents/OpenCV AI/coco.txt") as file:
    classes = file.read().strip().split("\n")


while True:
    retval,video = cap.read()
    if retval:
        bbox = (0,0,0,0)
        if (counter%10 == 0):
            boxes,confidences,classIDs,indices = getdetectionsfromnetwork()
            detectionrectangle(boxes,confidences,classIDs,indices)

        retval_tracker, bbox = tracker.update(video)
        if retval_tracker:
            (x1,y1,x2,y2)=bbox
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            cv2.rectangle(video, (x1, y1), (x2, y2), (255,0,0), 2)
        else:
            cv2.putText(video, "Tracking Failed", (0, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255))
            boxes,confidences,classIDs,indices = getdetectionsfromnetwork()
            detectionrectangle(boxes,confidences,classIDs,indices)
        #cap_writer.write(video)
        cv2.imshow("window",video)
        waitkey = cv2.waitKey(25)
        if (ord('q') == waitkey):
            break
        counter += 1
    else:
        break

cap.release()
cap_writer.release()
cv2.destroyAllWindows()