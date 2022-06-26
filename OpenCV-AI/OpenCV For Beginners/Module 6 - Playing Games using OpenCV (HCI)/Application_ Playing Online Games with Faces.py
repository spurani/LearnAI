import cv2
import numpy as np
import pyautogui as gui

prototxt_path='C:/Users/SP.000/Downloads/m6/Applications/model/deploy.prototxt'
model_path='C:/Users/SP.000/Downloads/m6/Applications/model/res10_300x300_ssd_iter_140000.caffemodel'
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

def play(prototxt_path, model_path):
	vidcap = cv2.VideoCapture(0)
	init = 0
	count = 0
	if(vidcap.isOpened() == False):
		exit()
	else:
		frame_width, frame_height = (vidcap.get(cv2.CAP_PROP_FRAME_WIDTH),vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		left_x, top_y = (int(frame_width // 2 - 150), int(frame_height // 2 - 200))
		right_x, bottom_y = (int(frame_width // 2 + 150), int(frame_height // 2 + 200))
		start_point=(left_x, top_y)
		end_point=(right_x, bottom_y)
		bbox = [left_x,right_x,top_y,bottom_y]
		while True:
			ret, frame = vidcap.read()
			if(ret):
				frame = cv2.flip(frame,1)
				frame = cv2.rectangle(frame,start_point,end_point,(0,255,0),1)
				detected_faces=detect(net,frame)
				frame=drawface(frame,detected_faces)
				if(count % 2 == 0):
					if(init == 0):
						if checkRect(detected_faces, bbox):
							init = 1
							cv2.putText(
							frame, 'Game is running', (100, 100),
							cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
							cv2.waitKey(10)
							last_mov = 'center'
							# Click to start the game.
							gui.click(x=500, y=500)
				else:
					move(detected_faces,bbox)
					cv2.waitKey(50)
				cv2.imshow("Live Video Feed",frame)
				count += 1
				key = cv2.waitKey(5)
				if(key == 27):
					break
					return
	vidcap.release()
	cv2.destroyAllWindows()

def detect(net, frame):
	detected_faces = []
	(h, w) = (frame.shape[0],frame.shape[1])
	blob = cv2.dnn.blobFromImage(cv2.resize(frame,(300, 300)),1,(300, 300),(104, 177, 123))
	net.setInput(blob)
	detections = net.forward()
	#print()
	for i in range(0,detections.shape[2]):
		confidence = detections[0,0, i, 2]
		if(confidence > 0.5):
			box = detections[0,0,i,3:7] * np.array([w,h,w,h])
			(startX, startY, endX, endY) = np.int0(box)
			detected_faces.append({'start': (startX, startY),'end':(endX,endY),'confidence':confidence})
	return detected_faces

def drawface(frame, detected_faces):
	for i in detected_faces:
		cv2.rectangle(frame,i['start'],i['end'],(35,0,0),thickness=2)
	return frame

def checkRect(detected_faces, bbox):
	for face in detected_faces:
		face_start = face['start']
		face_end = face['end']
		if(face_start[0] > bbox[0] and face_end[0] < bbox[1] and face_start[1] > bbox[2] and face_end[1] < bbox[3]):
				return True
	return False

def move(detected_faces, bbox):
	global last_move
	for face in detected_faces:
		x1, y1 = face['start']
		x2, y2 = face['end']
		if(checkRect(detected_faces,bbox)):
			left_move = 'center'
			return
		elif (left_move == center):
			if(x1 < bbox[0]):
				gui.press('left')
				last_move = 'left'
			if(x2 > bbox[1]):
				gui.press('right')
				last_move = 'right'
			if(y1 < bbox[2]):
				gui.press('top')
				last_move = 'top'
			if(y2 > bbox[3]):
				gui.bottom('bottom')
				last_move = 'bottom'
			if(last_move != 'center'):
				print(last_move)
play(prototxt_path,model_path)
