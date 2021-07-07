from tensorflow.keras.models import load_model
import os
import cv2
import numpy as np
model=load_model("catsvsdogs.hdf5")
count=0
dirname="/home/sp/Desktop/test1/"
labels={0:'cat',1:'dog'}
for i in os.listdir(dirname):
	if(count != 10):
		p=os.path.join(dirname,i)
		count+=1
		image1=cv2.imread(p)
		image=cv2.resize(image1,(32,32)).flatten()
		result=model.predict_classes(np.array([image/255.0]))
		cv2.putText(image1, labels[result[0]], (1,50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,0,0))
		cv2.imshow("f"+i,image1)
		print(labels[result[0]]," --- ",i,"---------")
	else:
		break
key=cv2.waitKey(0) & 0xFF
if(key == ord("q")):
	cv2.destroyAllWindows()
	exit()