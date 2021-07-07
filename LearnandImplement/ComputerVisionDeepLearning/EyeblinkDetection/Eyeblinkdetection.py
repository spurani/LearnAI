from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2

def eye_aspect_ratio(eye):
	A=dist.euclidean(eye[1],eye[5])##set 1 vertical eye distance
	B=dist.euclidean(eye[2],eye[4])##set 2 vertical eye distance
	C=dist.euclidean(eye[0],eye[3])##horizontal eye distance
	ear=(A+B)/(2.0*C)
	return ear

ap = argparse.ArgumentParser()
ap.add_argument("-p","--shape-predictor",required=True,help="path to facial keypoints detection")
#ap.add_argument("-v","--video",required=True,help="path to video file")
args=vars(ap.parse_args())
print(args)
EYE_AR_THRESH=0.3
EYE_AR_CONSEC_FRAME=3
COUNTER=0
TOTAL=0
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor(args["shape_predictor"])
(lStart,lEnd)=face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart,rEnd)=face_utils.FACIAL_LANDMARKS_IDXS['right_eye']
vs=VideoStream(0).start()
fileStream=False
time.sleep(1.0)
while True:
	if fileStream and not vs.more():
		break
	frame=vs.read()
	frame=imutils.resize(frame,width=450)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	rects=detector(gray,0)
	for (i,rect) in enumerate(rects):
		shape=predictor(gray,rect)
		shape=face_utils.shape_to_np(shape)
		leftEye=shape[lStart:lEnd]
		rightEye=shape[rStart:rEnd]
		leftEAR=eye_aspect_ratio(leftEye)
		rightEAR=eye_aspect_ratio(rightEye)
		ear=(leftEAR+rightEAR) / 2.0
		leftEyeHull=cv2.convexHull(leftEye)
		rightEyeHull=cv2.convexHull(rightEye)
		cv2.drawContours(frame,[leftEye],-1,(255,0,0),2)
		cv2.drawContours(frame, [rightEye], -1, (255,0,0),2)
		if(ear<EYE_AR_THRESH):
			COUNTER+=1
		else:
			if(COUNTER>=EYE_AR_CONSEC_FRAME):
				TOTAL+=1
			COUNTER=0
		cv2.putText(frame,"Blinks: {}".format(TOTAL),(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),1)
		cv2.putText(frame,"EAR: {}".format(ear),(100,100),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),1)
	cv2.imshow("vid",frame)
	key=cv2.waitKey(1) & 0xFF
	if(key==ord("q")):
		break
cv2.destroyAllWindows()
vs.stop()