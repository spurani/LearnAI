# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 04:11:49 2022

@author: SP
"""

import cv2
import numpy as np

net = cv2.dnn.readNetFromCaffe("deploy.prototxt","res10_300x300_ssd_iter_140000_fp16.caffemodel")
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel('model/lbfmodel.yaml')
frame_count = 0
frame_calib = 30
sum_ear = 0
state_prev = state_curr = 'open'
BLINK = 0

def calculate_distance(A, B):
    distance = ((A[0] - B[0])**2+(A[1] - B[1])**2)**0.5
    return distance

def get_eye_aspect_ratio(landmarks):
    vert_dist_1right = calculate_distance(landmarks[37], landmarks[41])
    vert_dist_2right = calculate_distance(landmarks[38], landmarks[40])
    vert_dist_1left = calculate_distance(landmarks[43], landmarks[47])
    vert_dist_2left = calculate_distance(landmarks[44], landmarks[46])
    
    horz_dist_right = calculate_distance(landmarks[36], landmarks[39])
    horz_dist_left = calculate_distance(landmarks[42], landmarks[45])
    
    EAR_left = (vert_dist_1left + vert_dist_2left) / (2.0 + horz_dist_left)
    EAR_right = (vert_dist_1right + vert_dist_2right) / (2.0 + horz_dist_right)
    
    ear = (EAR_left + EAR_right)
    return ear
vidcap = cv2.VideoCapture(0)
if(vidcap.isOpened()):    
    while True:
        retval, frame = vidcap.read()
        if(retval):
            blob = cv2.dnn.blobFromImage(frame,1,(300,300),[104,117,123],swapRB=False,crop=False)
            net.setInput(blob)
            detections = net.forward()
            detections_final = detections[0][0]
            faces = []

            for i in detections_final:
                if(i[2] > 0.9):
                    h, w = frame.shape[:2]
                    x1 = int(i[3] * w)
                    y1 = int(i[4] * h)
                    x2 = int(i[5] * w)
                    y2 = int(i[6] * h)
                    face_w = x2 - x1
                    face_h = y2 - y1
                    faces.append((x1,y1,face_w,face_h))
                    faces_detected = np.array(faces,dtype='int')
                    #print(faces_detected)
                    retval1, landmarks = landmark_detector.fit(frame,faces_detected)
                    landmarks_pt = landmarks[0][0].astype('int')
                    ear = get_eye_aspect_ratio(landmarks_pt)
                    
                    for i in range(len(landmarks_pt)):
                        if(i >= 36 and i <= 47):
                            cv2.circle(frame,(landmarks_pt[i][0],landmarks_pt[i][1]),1,(0,255,255),1,cv2.LINE_AA)
                            if(frame_count < frame_calib):
                                frame_count += 1
                                sum_ear = sum_ear + ear
                            elif(frame_count == frame_calib):
                                    frame_count += 1
                                    avg_ear = sum_ear//frame_count
                                    HIGHER_TH = 0.90 * avg_ear
                                    LOWER_TH = 0.70 * avg_ear
                            else:
                                if(ear < LOWER_TH):
                                    state_curr = 'closed'
                                elif(ear > HIGHER_TH):
                                    state_curr = 'open'
                                if(state_prev == 'closed' and state_curr == 'open'):
                                    BLINK += 1
                                state_prev = state_curr
                                
                            cv2.putText(frame, "Blink Counter: {}".format(BLINK), (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
                                    1.5, (0, 0, 255), 4, cv2.LINE_AA)
        else:
            break
        key = cv2.waitKey(1)
        cv2.imshow("Window",frame)
        if(key == ord('q')):
            break

vidcap.release()
cv2.destroyAllWindows()