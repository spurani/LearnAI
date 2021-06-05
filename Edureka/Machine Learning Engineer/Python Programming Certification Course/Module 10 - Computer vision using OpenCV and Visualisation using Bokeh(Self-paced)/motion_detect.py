import cv2,time

video=cv2.VideoCapture(0)

check,frame=video.read()

#print(check)
#print(frame)

time.sleep(3)

#

cv2.imshow('Capturing',frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows

#Code
import cv2,time

video=cv2.VideoCapture(0)
a=1

while True:
    a=a+1
    check,frame=video.read()
    print(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing',frame)
    key=cv2.waitKey(1)
    if(key==ord('q')):
        break

print(a) # This will print the number of frames
video.release()
cv2.destroyAllWindows


#code : Motion detector

import cv2,time

first_frame=None

video=cv2.VideoCapture(0)


while True:

    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame==None:
        first_frame=gray
        continue

delta_frame=cv2.absdiff(first_frame,gray)

thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)

(_,cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for contour in cnts:
    if cv2.contourArea(contour)<1000:
        continue
    (x,y,w,h)=cv2.boundingRect(contour)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255),3)

cv2.imshow('frame',frame)
cv2.imshow('Capturing',gray)
cv2.imshow('delta',delta_frame)
cv2.imshow('thresh',thresh_delta)

key=cv2.waitKey(1)
if key==ord('q'):
    break

video.release()
cv2.destroyAllWindows



#slide 81-85:

#Slide 81
import pandas
import cv2

first_frame=None
status_list=[None, None]
times=[]

df=pandas.DataFrame(columns=["Start","End"])

video=cv2.VideoCapture(0)

while True:
    check, frame=video.read()
    status=0
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

#Slide 82
(_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAl, cv2.CHAIN_APPROX_SIMPLE)

for contour in cnts:
    if cv2.contourArea(contour)< 10000:
        continue
    status=1

#83
(x,y,w,h)=cv2.boundingRect(contour)
cv2.rectangel(frame, (x,y), (x+w, y+h),(0,255,0),3)
if status[-1]==1 and status_list[-2]==0:
    times.append(datetime.now())

if status[-1]=0 and status_list[-2]==1:
    times.append(datetime.now())

#84
print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows


#85

from motion_detector import df
from bokeh.plotting import figure, show, output_file

df["Start_string"]=df["Start"].dt.strftime["%Y-%m-%d %H:%M:%S"]
df["End_sring"]=df["End"].dt.strftime["%Y-%m-%d %H:%M:%S"]

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_strings")])
p.add_tools(hover)

q=p.quad(left="Start",right="End", bottom=0, top=1, color="Red", source=cds)


output_file("Graph1.html")
show(p)
