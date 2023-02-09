# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import dlib

landmarkDetector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def VidCap():
    vidcap = cv2.VideoCapture(0)

    while True:
        if(vidcap.isOpened()):
            retval, frame = vidcap.read()
            if(retval):
                key = cv2.waitKey(1)
                if(ord('q') == key or ord('Q') == key):
                    break
                else:
                    detect_faces(frame)
                    cv2.imshow("Frame",frame)
        else:
            break
    
    cv2.destroyAllWindows()
    vidcap.release()

def detect_faces(vid_feed):
    h, w = vid_feed.shape[:2]
    cascade = cv2.CascadeClassifier()
    cascade.load("C:\\Users\\SP.000\\Documents\\OpenCV AI\\OpenCV For Beginners\\Module 14 - Face and Landmarks Detection\\model\\haarcascade_frontalface_default.xml")
    objects = cascade.detectMultiScale(vid_feed)
    for i in objects:
            x1, y1, x2, y2 = int(i[0]), int(i[1]), int(i[2]), int(i[3])
            cv2.rectangle(vid_feed, (x1, y1, x2, y2), (0,255,255), 2, cv2.LINE_AA)
            rect = dlib.rectangle(x1, y1, x2, y2)
            detect_facial_landmarks(vid_feed,rect)

def detect_facial_landmarks(vid_feed,rect):
    landmarks = landmarkDetector(vid_feed,rect)
    num_parts = landmarks.num_parts
    for i in range(0,num_parts):
        print(i)
        (x, y) = landmarks.part(i).x, landmarks.part(i).y
        cv2.circle(vid_feed,(x,y),1,(255,100,45),-1)
        #cv2.imshow("Frame",upd_frame)

VidCap()
