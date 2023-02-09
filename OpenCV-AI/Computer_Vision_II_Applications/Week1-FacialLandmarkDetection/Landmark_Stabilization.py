# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import dlib
import numpy as np
import math

landmarkDetector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facedetector = dlib.get_frontal_face_detector()

winName = "Stabilized facial landmark detector"
winSize = 101
maxLevel = 10
fps = 30.0

# Initializing the parameters
points=[]
pointsPrev=[]
pointsDetectedCur=[]
pointsDetectedPrev=[]

eyeDistanceNotCalculated = True
eyeDistance = 0
isFirstFrame = True
# Initial value, actual value calculated after 100 frames
fps = 10
showStabilized = False
count =0
def VidCap():
    global showStabilized
    vidcap = cv2.VideoCapture(0)
    retval, oldframe = vidcap.read()
    oldframe_gray = cv2.cvtColor(oldframe, cv2.COLOR_BGR2GRAY)
    while True:
        if(vidcap.isOpened()):
            retval, frame = vidcap.read()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if(retval):
                key = cv2.waitKey(1)
                if key==32:
                    showStabilized = not showStabilized
                if(ord('q') == key or ord('Q') == key):
                    break
                else:
                    detect_faces(frame, oldframe)
                    cv2.imshow("Frame",frame)

        else:
            break

    cv2.destroyAllWindows()
    vidcap.release()

def detect_faces(vid_feed, oldvid_feed):
    faces = facedetector(vid_feed,0)
    if(len(faces) > 0):
        for i in faces:
            top = i.top()
            bottom = i.bottom()
            left = i.left()
            right = i.right()
            cv2.rectangle(vid_feed,(top,left),(bottom,right),(0,255,155),1,cv2.LINE_AA)
            detect_facial_landmarks(vid_feed,dlib.rectangle(top,left,bottom,right), oldvid_feed)

def detect_facial_landmarks(vid_feed,rect,oldvid_feed):
    landmarks = landmarkDetector(vid_feed,rect)
    eyeDistance = interEyeDistance(landmarks)
    (pointsArr, pointsPrevArr, pointsDetectedCur, points, pointsDetectedPrev) = get_prev_next_pts(landmarks)
    num_parts = landmarks.num_parts
    #print(pointsDetectedCur)
    #print(pointsDetectedPrev)
    st_points, dotRadius = calc_Optical_Flow(oldvid_feed, vid_feed, pointsArr,pointsPrevArr, eyeDistance, num_parts, pointsDetectedPrev, pointsDetectedCur)
    draw_circle(st_points, pointsDetectedCur, dotRadius, vid_feed)

def interEyeDistance(landmarks):
    leftEyeLeftCoord = (landmarks.part(36).x, landmarks.part(36).y)
    rightEyeRightCoord = (landmarks.part(45).x, landmarks.part(45).y)
    distance = int(cv2.norm(np.array(leftEyeLeftCoord) - np.array(rightEyeRightCoord)))
    return distance

def get_prev_next_pts(landmarks):
    global points
    global pointsDetectedCur
    num_parts = landmarks.num_parts
    pointsPrev=[]
    pointsDetectedPrev=[]
    for i in range(0,num_parts):
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        if(isFirstFrame):
            #isFirstFrame = False
            pointsPrev.append((x,y))
            pointsDetectedPrev.append((x,y))
            #print(pointsPrev)
            print(i)
        else:
            pointsPrev = points
            pointsDetectedPrev = pointsDetectedCur

    points = []
    pointsDetectedCur = []
    for i in range(0,num_parts):
        #print(i)
        x = landmarks.part(i).x
        y = landmarks.part(i).y
        pointsDetectedCur.append((x,y))
        points.append((x,y))
    pointsArr = np.array(points,np.float32)
    pointsPrevArr = np.array(pointsPrev,np.float32)
    print(points)
    print(pointsPrevArr)
    return (pointsArr, pointsPrevArr, pointsDetectedCur, points, pointsDetectedPrev)

def calc_Optical_Flow(oldframe_gray, frame_gray, pointsArr, pointsPrevArr, eyeDistance, num_parts, pointsDetectedPrev, pointsDetectedCur):
    global eyeDistanceNotCalculated
    if(eyeDistanceNotCalculated > 100):
        eyeDistanceNotCalculated = False

    if(eyeDistance > 100):
        dotRadius = 3
    else:
        dotRadius = 2
    
    sigma = eyeDistance * eyeDistance / 400
    s = 2*int(eyeDistance/4)+1
    #  Set up optical flow params
    lk_params = dict(winSize  = (s, s), maxLevel = 5, criteria = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 20, 0.03))
    pointsArr,status, err = cv2.calcOpticalFlowPyrLK(oldframe_gray,frame_gray,pointsPrevArr,pointsArr,**lk_params)
    # Converting to float
    pointsArrFloat = np.array(pointsArr,np.float32)

    # Converting back to list
    points = pointsArrFloat.tolist()
    st_points = []
    for k in range(0, num_parts):
        d = cv2.norm(np.array(pointsDetectedPrev[k]) - np.array(pointsDetectedCur[k]))
        alpha = math.exp(-d * d/ sigma)
        st_points.append((1 - alpha) * np.array(pointsDetectedCur[k]) + alpha * np.array(points[k]))
    return st_points, dotRadius

def draw_circle(st_points, pointsDetectedCur, dotRadius, im):
    global isFirstFrame
    if showStabilized is True:
        for p in points:
          cv2.circle(im,(int(p[0]),int(p[1])),dotRadius, (255,0,0),-1)
    else:
        for p in pointsDetectedCur:
          cv2.circle(im,(int(p[0]),int(p[1])),dotRadius, (0,0,255),-1)
    isFirstFrame=True
VidCap()
