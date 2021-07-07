# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:34:07 2021

@author: SP
"""

import argparse
import cv2
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to image",required=True)
args=vars(ap.parse_args())
rows = open("synsets.txt").read().strip().split("\n")
classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]
net=cv2.dnn.readNetFromCaffe("bvlc_googlenet.prototxt.txt","bvlc_googlenet.caffemodel")
image=cv2.imread(args["image"])
blob=cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))
net.setInput(blob)
preds=net.forward()
idx = np.argmax(preds[0])
print(classes[idx])
cv2.putText(image,'{}: {:.2f}'.format(classes[idx],preds[0][idx]),(50,100),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),2)
cv2.imshow("image",cv2.resize(image,(500,500)))
cv2.waitKey(0)