# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:58:29 2022

@author: SP
"""
'''Import libraries'''
import cv2

'''Load the pretrained model'''
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000_fp16.caffemodel")

'''Create videocapture object'''
vidcap = cv2.VideoCapture(0)
d = []
while True:
    if(vidcap.isOpened()):
        retval, frame = vidcap.read()
        height, width = frame.shape[:2]
        if(retval):
            '''Convert image into blob'''
            blob = cv2.dnn.blobFromImage(image=frame,scalefactor=1.0,size=(300,300),mean=[104,117,123],swapRB=False,crop=False)
            '''Pass the blob to the network. Setting the blob as input for the network'''
            net.setInput(blob)
            '''Make a forward pass through the network. 
            Forward pass means network will take the input and pass it through its pretrained weights stored in every layer'''
            detections = net.forward()
            detections_final = detections[0][0]
            '''
            net.forward returns an array of shape (1,1,200,7)
            here it gives us 200 detections based on the frame this value differs from scene to scene not FRAME to FRAME. So for example I provide another type of scene there might be more or less detections
            but the last index value 7 will always remain constant. So we have to loop through all 200 detections and find out which one of that has highest confidence and only show that detection.
            As we dont want to false detections with less confidence.
            In each detection array we have [batchId, classId, confidence, left, top, right, bottom]
            '''
            for i in detections_final:
                ''' Extract and check if confidence is above certain threshold to get valid results'''
                if(i[2] >= 0.5):
                    x1 = int(i[3] * width)
                    y1 = int(i[4] * height)
                    x2 = int(i[5] * width)
                    y2 = int(i[6] * height)
                    confidence = i[2] * 100
                    cv2.putText(frame,"Confidence: {confidence:.2f}".format(confidence=confidence),(x1,y1-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2,cv2.LINE_AA)
                    cv2.rectangle(frame,(x1, y1),(x2, y2),(0,255,255),2,cv2.LINE_AA)
            cv2.imshow("Face Detection Demo",frame)
            key = cv2.waitKey(1)
            if(key == ord('q')):
                break
        else:
            break
    else:
        break
cv2.destroyAllWindows()
vidcap.release()
