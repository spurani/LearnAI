# -*- coding: utf-8 -*-
"""
Created on Mon May 23 09:47:13 2022

@author: SP

Lucas Kannada Optical Flow is used for Motion Estimation and Improving the facial Landmarks. We will explore how this concept
can be implemented.
"""

import cv2
import numpy as np

lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

def video_Capture():
    vid_cap = cv2.VideoCapture("cycle.mp4")
    retval, old_feed = vid_cap.read()
    old_feed_gray = cv2.cvtColor(old_feed,cv2.COLOR_BGR2GRAY)
    oldPts = get_detected_corner_pts(old_feed_gray)
    mask = np.zeros_like(old_feed)
    colors = np.random.randint(0,255,(len(oldPts),3))
    while True:
        if(vid_cap.isOpened()):
            retval, feed = vid_cap.read()
            if(retval):
                key = cv2.waitKey(10)
                #feed_gray = cv2.cvtColor(feed,cv2.COLOR_BGR2GRAY)
                #curr_corners = get_detected_corner_pts(feed_gray)
                nextPts, status, err = cv2.calcOpticalFlowPyrLK(old_feed, feed, oldPts,None, **lk_params)
                good_new_nextPts = nextPts[status == 1]
                good_old_prevPts = oldPts[status == 1]
                for i,(new, old) in enumerate(zip(good_new_nextPts, good_old_prevPts)):
                    (ax, ay) = new.ravel()
                    (bx, by) = old.ravel()
                    cv2.line(mask, (ax,ay),(bx,by), colors[i].tolist(),2,cv2.LINE_AA)
                    cv2.circle(feed,(ax,ay),3,255,-1)
                display_frame = cv2.add(mask, feed)
                cv2.imshow("Feed",display_frame)
                print(oldPts.shape, oldPts.ndim)
                print(good_new_nextPts.shape, good_new_nextPts.ndim)
                #print(oldPts)
                #print(good_new_nextPts)
                oldPts = good_new_nextPts.reshape(-1,1,2)
                old_feed = feed.copy()
                print("--------------------------------------------------")
                print(oldPts.shape, oldPts.ndim)
                print(good_new_nextPts.shape, good_new_nextPts.ndim)
                #print(oldPts)
                #print(good_new_nextPts)
                #break
                if(ord('q') == key):
                    break
            else:
                print("No video input data found")
                break
        else:
            print("No video input source found")
            break
    vid_cap.release()
    cv2.destroyAllWindows()

def get_detected_corner_pts(frame_gray):
    corners = cv2.goodFeaturesToTrack(frame_gray,100,0.3,7,7)
    return corners
video_Capture()