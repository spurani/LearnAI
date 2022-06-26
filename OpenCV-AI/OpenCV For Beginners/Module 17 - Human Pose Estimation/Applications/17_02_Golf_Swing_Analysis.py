import cv2
import time
import math
import mediapipe as mp
import numpy as np

# Create video capture object.
file_name  = 'Reference_Swing_DTL.mp4'
print(file_name[:-4])
video_cap = cv2.VideoCapture(file_name)
if not video_cap.isOpened():
    print('Unable to open: ' + file_name)

# Create a video writer object.
fps = int(video_cap.get(cv2.CAP_PROP_FPS))
frame_w = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_h = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_w, frame_h)

video_out_file = file_name[:-4] + '_out_landmarks.mp4'
video_output = cv2.VideoWriter(video_out_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)
video_output = cv2.VideoWriter(video_out_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)

# Process image frames and extract landmark coordinates.
# BGR Colors
color_light  = (255, 255, 0)
color_marks  = (0, 255, 255)
color_join   = (0, 20, 200)

# In a more advanced application the initial position of
# the golf ball would be automatically detected.
ball_pos_x = 650
ball_pos_y = 927

mp_pose = mp.solutions.pose
print('Processing frames please wait..')
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    while True:

        has_frame, frame = video_cap.read()
        if not has_frame:
            break

        # Convert the BGR image to RGB.
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image frame.
        keypoints = pose.process(frame)
        landmarks = keypoints.pose_landmarks
        enum_pose  = mp_pose.PoseLandmark

        # Convert the image back to BGR.
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if landmarks is not None:

            # Right ear.
            r_ear_x = int(landmarks.landmark[enum_pose.RIGHT_EAR].x * frame_w)
            r_ear_y = int(landmarks.landmark[enum_pose.RIGHT_EAR].y * frame_h)
            r_ear_p = np.array([r_ear_x, r_ear_y])

            # Right wrist.
            r_wrist_x = int(landmarks.landmark[enum_pose.RIGHT_WRIST].x * frame_w)
            r_wrist_y = int(landmarks.landmark[enum_pose.RIGHT_WRIST].y * frame_h)
            r_wrist_p = np.array([r_wrist_x, r_wrist_y])

            # Right hip.
            r_hip_x = int(landmarks.landmark[enum_pose.RIGHT_HIP].x * frame_w)
            r_hip_y = int(landmarks.landmark[enum_pose.RIGHT_HIP].y * frame_h)
            r_hip_p = np.array([r_hip_x, r_hip_y])

            # Join landmarks.
            cv2.line(frame, (r_hip_p[0], r_hip_p[1] ), (r_ear_p[0], r_ear_p[1]), color_join, 2, cv2.LINE_AA)
            cv2.line(frame, (r_hip_p[0], r_hip_p[1] ), (r_wrist_p[0], r_wrist_p[1]), color_join, 2, cv2.LINE_AA)
            cv2.line(frame, (r_ear_p[0], r_ear_p[1]), (r_wrist_p[0], r_wrist_p[1]), color_join, 2, cv2.LINE_AA)
            cv2.line(frame, (ball_pos_x, ball_pos_y), (r_wrist_p[0], r_wrist_p[1]), color_light, 2, cv2.LINE_AA)

            # Draw landmarks.
            cv2.circle(frame, (r_ear_p[0], r_ear_p[1]), 3, color_marks, -1)
            cv2.circle(frame, (r_wrist_p[0], r_wrist_p[1]), 3, color_marks, -1)
            cv2.circle(frame, (r_hip_p[0], r_hip_p[1] ), 3, color_marks, -1)
            cv2.circle(frame, (ball_pos_x, ball_pos_y), 3, color_marks, -1)

            video_output.write(frame)
print('Processing completed.')
video_cap.release()
video_output.release()
