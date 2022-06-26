#Application: Sunglass Filter realtime
# 0) Install Dlib, imutils and Download http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
# 1) Load all the necessary libraries
# 2) Perform preprocessing on transparent image of sunglass(BGRA)
# 3) Detect face keypoints/landmarks/features
# 4) Get location coordinates from facial landmarks
# 5) Crop the image based on the location of facial landmarks from boundingRect
# 6) Perform masking on croppedimage and sunglassimage with 3channel(BGR)
# 7) Replace the finalcropped image with glasses with the specific part of videoframe by passing extracted location from bounding box
import cv2
import numpy as np
import dlib
from imutils import face_utils

vid=cv2.VideoCapture(0)
glass=cv2.imread("sunglass.png",-1)
glass=cv2.resize(glass,(300,100))
glassBGR=glass[:,:,0:3]###BGR channel
glassMask1=glass[:,:,3]##Alpha channel
glassMask=cv2.merge((glassMask1,glassMask1,glassMask1))
glassMask=np.uint8(glassMask/255)
# Create Dlib detector object which will detect face
detector=dlib.get_frontal_face_detector()
# Create Dlib predictor object which will extract face features from detected face
predictor=dlib.shape_predictor("/home/sp/Desktop/shape_predictor_68_face_landmarks.dat")
# Below is the list of landmark keypoints which I would like to detected on image and will be considered are ROI
# For reference https://bit.ly/3lgFwUV
listofpoints=[0,1,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,36,37,38,39,40,41,42,43,44,45,46,47]
while True:
	ret,frame=vid.read()
	#Get the Facial Detection whole face for example if an videoframe or image has 1 face it will only detect one whole face, if it has 2 faces in an image or video frame it will detect 2 whole faces
	detections=detector(frame)
	eyepoints=[]
	for k, d in enumerate(detections):
		#cv2.rectangle(frame, (d.left(),d.top()), (d.right(),d.bottom()), (0,255,0),3)
		#Get shapes from the detected face such as eyes, nose, eyebros, mouth, jaw, lips much more
		shape=predictor(frame,d)##This returns an object
		shape=face_utils.shape_to_np(shape)## Converting Dlib shape predictor object to array
		for i,(x,y) in enumerate(shape):
			if(i in listofpoints):
				#Adding location coordiantes of detected landmark keypoints from listofpoints list to new list named eyepoints
				eyepoints.append((x,y))
				#cv2.circle(frame,(x,y), 3, (255,0,255))
	if(len(eyepoints) != 0):
		eyepoints=np.array(eyepoints)
		x,y,w,h=cv2.boundingRect(eyepoints)#Convert keypoints into boundingRect so that we get an enclosing part
		roi=frame[y:y+h,x:x+w]#Note above boundingBect returns (x(column),y(row)) top-left coordinate w->width,h->height of rectangle bounding
		#cv2.imshow("roi", roi)
		# Below we are resizing glassMask and glassBGR is only becuase we have to match the exact size with above roi extracted from detected bounding Rect
		glassMaskresized=cv2.resize(glassMask,(roi.shape[1],roi.shape[0]))
		maskedeye=cv2.multiply((1-glassMaskresized),roi)
		cv2.imshow("maskedeye", maskedeye)
		glassresizedBGR=cv2.resize(glassBGR,(roi.shape[1],roi.shape[0]))
		glassMaskedBGR=cv2.multiply(glassresizedBGR,glassMaskresized)
		finalroi=cv2.add(maskedeye,glassMaskedBGR)
		frame[y:y+h,x:x+w]=finalroi
		cv2.imshow("frame", frame)
	if(cv2.waitKey(1) == ord('q')):
		break
vid.release()
cv2.destroyWindow("frame")
