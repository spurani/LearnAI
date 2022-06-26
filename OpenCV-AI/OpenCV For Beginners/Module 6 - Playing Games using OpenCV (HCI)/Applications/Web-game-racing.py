'''
This is simplified version of the web-game. 
It only uses Left and Right movement and can be used for racing games
'''


import cv2
import numpy as np
import pyautogui as gui
import time

# Set  keypress  delay  to  0
gui.PAUSE = 0


# Loading the model
model_path = './model/res10_300x300_ssd_iter_140000.caffemodel'
prototxt_path = './model/deploy.prototxt'
def detect(net,frame):
	'''
	Function to detect the faces in the frame
	
	returns: list of faces in the frame
				here each face is a dictionary of format- 
				{'start': (startX,startY), 'end': (endX,endY), 'confidence': confidence}
	'''
	detected_faces=[]
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),1.0,(300, 300), (104.0, 177.0, 123.0))
	net.setInput(blob)
	detections = net.forward()
	for i in range(0, detections.shape[2]):
		confidence = detections[0,0,i,2]
		if confidence > 0.5:
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")
			detected_faces.append({'start':(startX,startY),'end':(endX,endY),'confidence':confidence})
	return detected_faces

def drawFace(frame, detected_faces):
	'''
	Function to draw rectangular box over detected faces

	returns: frame with rectangular boxes over detected faces
	'''
	for face in detected_faces:
		cv2.rectangle(frame, face['start'], face['end'],(0, 255, 0), 10)
		y = face['start'][1] - 10 if face['start'][1] - 10 > 10 else face['start'][1] + 10
		
	return frame

def checkRect(detected_faces, bbox):
	'''
	Function to check that a detected face is inside the bounding box at the center of the frame.

	returns: True or False.
	'''
	for face in detected_faces:
		x1, y1 = face['start']
		x2, y2 = face['end']
		if x1 > bbox[0] and x2 < bbox[1]:
			if y1 > bbox[3] and y2 < bbox[2]:
				return True
	return False


def move(detected_faces, bbox):
	'''
	Function to press the correct button depending on the position of detected face and bbox.

	The last_mov check is added for making sure the character doesnt keep drifting in the previous detection.
	'''
	for face in detected_faces:
		x1, y1 = face['start']
		x2, y2 = face['end']

		# Center
		if checkRect(detected_faces, bbox):
			pass
	
		# Left
		if x1 < bbox[0]:
			gui.keyDown('left')
		else:
			gui.keyUp('left')
								
		# Right
		if x2 > bbox[1]:
			gui.keyDown('right')
		else:
			gui.keyUp('right')
		
			
				

def play(prototxt_path, model_path):
	# Used to record the time when we processed last frame.
	prev_frame_time = 0
	# Used to record the time at which we processed current frame.
	new_frame_time = 0

	net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
	cap = cv2.VideoCapture(0)

	# Counter for skipping frame.
	count = 0
	
	# Used to initialise the game. 
	init = 0

	# Getting the Frame width and height.
	frame_width, frame_height = int(cap.get(3)), int(cap.get(4))

	# Co-ordinates of the bounding box on frame
	left_x, top_y = frame_width // 2 - 150, frame_height //2 - 200
	right_x, bottom_y = frame_width//2 + 150, frame_height //2 + 200
	bbox = [left_x, right_x, bottom_y, top_y]
	
	while not cap.isOpened():
		cap = cv2.VideoCapture(0)
	
	while True:
		fps = 0 
		ret, frame = cap.read()
		
		if not ret:
			return 0
		
		frame = cv2.flip(frame,1)
		# Detect the face.
		detected_faces = detect(net,frame)
		# Draw bounding box around detected faces.
		frame = drawFace(frame, detected_faces)
		# Drawing the control rectangle in the center of the frame.
		frame = cv2.rectangle(frame, (left_x, top_y), (right_x, bottom_y), (0,0,255), 5)
		
		# Skipping every alternate frame
		if count % 2 == 0:	
			# For first pass.	
			if init == 0:
				# If face is inside the control rectangle.
				if checkRect(detected_faces, bbox):
					init = 1
					cv2.putText(frame, 'Game is running', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255 ,0), 2)
					cv2.waitKey(10)
					# Click to start the game.
					gui.click(x = 500, y = 500)
			else:

				move(detected_faces, bbox)
				cv2.waitKey(50)
		# Calculating the FPS
		new_frame_time = time.time()
		fps = int(1 / (new_frame_time - prev_frame_time))
		prev_frame_time = new_frame_time

		frame = cv2.putText(frame, str(fps) + 'FPS', (200,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
		cv2.imshow('camera_feed', frame)
		count += 1
				
		k = cv2.waitKey(5)
		if k == 27:
		    return

if __name__ == "__main__":
	last_mov = ''
	play(prototxt_path, model_path)
