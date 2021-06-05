import cv2,time

video = cv2.VideoCapture(0)

# Check - Boolean Dtype
# Frame - NumPy Array
check, frame = video.read()

print(check)
print(frame)

time.sleep(3)

video.release()