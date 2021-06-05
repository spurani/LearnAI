#Slide 52
import cv2

#Create a cascadeClassifier Object
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Reading the image as it is
img=cv2.imread("photo.jpg")

#Reading the image as gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Search the co-ordinates of the image
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

print(type(faces))
print(faces)


#Slide 53
#Create a CascaseClassifier Object
face_cascade=cv2.CacadeClassifier("haarcascade_frontalface_default.xml")

#Reading the image as gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)





#Slide 54

#Search the co-ordinates of the image
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)


#Slide 55
print(type(faces))
print(faces)



for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)