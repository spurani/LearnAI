import cv2
import mediapipe as mp

# Read the test image.
img = cv2.imread("Tiger_Woods.png")

img_width = img.shape[1]
img_height = img.shape[0]

# Display original image.
cv2.imshow('Tiger Woods', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Initialize mMediaPipe objects.
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

with mp_pose.Pose(static_image_mode=True) as pose:
    # Make a copy of the original image.
    annotated_img = img.copy()

    # Process image.
    results = pose.process(img)

    # Draw landmarks.
    circle_radius = int(.007 * img_height)  # Scale landmark circles as percentage of image height.

    # Specify landmark drawing style.
    point_spec = mp_drawing.DrawingSpec(color=(220, 100, 0), thickness=-1, circle_radius=circle_radius)

    # Draw landmark points.
    mp_drawing.draw_landmarks(annotated_img,
                              landmark_list=results.pose_landmarks,
                              landmark_drawing_spec=point_spec)

# Display the annotated image.
cv2.imshow('Landmarks drawn', annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Make a copy of the original image.
annotated_img = img.copy()

# Specify landmark connections drawing style.
line_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)

# Draw both landmark points and connections.
mp_drawing.draw_landmarks(annotated_img,
                          landmark_list=results.pose_landmarks,
                          connections=mp_pose.POSE_CONNECTIONS,
                          landmark_drawing_spec=point_spec,
                          connection_drawing_spec=line_spec)

# Display the annotated image.
cv2.imshow('Landmarks drawn', annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Acquire the landmark coordinates for the left and right hips.
r_hip_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * img_width)
r_hip_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * img_height)

l_hip_x = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x * img_width)
l_hip_y = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * img_height)

print('Right hip coordinates : (', r_hip_x,',',r_hip_y,')' )
print('Left hip coordinates  : (', l_hip_x,',',l_hip_y,')' )