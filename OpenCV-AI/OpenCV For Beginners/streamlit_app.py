# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 06:22:07 2022

@author: SP
"""

import cv2
import streamlit as st
import numpy as np
from PIL import Image

st.title("OpenCV Deep Learning based Face Detection")
img_file_buffer = st.file_uploader("Choose a file",type=["jpg","jpeg","png"])

def load_model():
    net = cv2.dnn.readNetFromCaffe("C:/Users/SP.000/Downloads/m6/Applications/model/deploy.prototxt","C:/Users/SP.000/Downloads/m6/Applications/model/res10_300x300_ssd_iter_140000.caffemodel")
    return net

def detectFaceOpenCVDNN(frame,net):
    blob = cv2.dnn.blobFromImage(frame,1,(300,300),(104,117,123),False, False)
    net.setInput(blob)
    detections = net.forward()
    return detections

def process_detections(frame, detections,confidence_threshold=0.5):
    h = frame.shape[0]
    w = frame.shape[1]
    bboxes = []
    #print(detections[0][0][0])
    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]
        if(confidence > confidence_threshold):
            x1 = int(detections[0,0,i,3] * w)
            y1 = int(detections[0,0,i,4] * h)
            x2 = int(detections[0,0,i,5] * w)
            y2 = int(detections[0,0,i,6] * h)
            bboxes.append([x1,y1,x2,y2])
            bb_line_thickness = max(1, int(round(h / 200)))
            cv2.rectangle(frame,(x1,y1),(x2,y2),bb_line_thickness,cv2.LINE_AA)
    return frame, bboxes

if img_file_buffer is not None:
    raw_bytes = np.asarray(bytearray(img_file_buffer.read()),dtype=np.int8)
    image = cv2.imdecode(raw_bytes,cv2.IMREAD_COLOR)
    net = load_model()
    placeholders = st.columns(2)
    placeholders[0].image(image,channels='BGR')
    placeholders[0].text("Input Image")
    conf_threshold = st.slider("SET Confidence Threshold",min_value=0.0,max_value=1.0,step=0.1,value=0.5)
    detections = detectFaceOpenCVDNN(image,net)
    frame, bboxes = process_detections(image,detections,confidence_threshold=conf_threshold)
    placeholders[1].image(frame, channels='BGR')
    placeholders[1].text('Output Image')