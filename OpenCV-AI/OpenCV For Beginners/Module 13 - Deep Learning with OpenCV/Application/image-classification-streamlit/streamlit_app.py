'''
This web app will serve the purpose for Image Classification
'''
import cv2
import streamlit as st
import numpy as np

#Load the DenseNet model trained on ImageNet dataset which has around 1000 classes using Caffe 
net = cv2.dnn.readNetFromCaffe("../../OpenCV DNN Module/DenseNet_121.prototxt","../../OpenCV DNN Module/DenseNet_121.caffemodel")
labels = []

#Prepare class names or labels associated with class ids
with open("labels.txt",'r') as label:
    for i in label.readlines():
        labels.append(i)

# This is a utility function which returns probability score and class name
def get_score_probability(detection_array):
    detections = detection_array[0]
    detections_final = detections.reshape(1000,1)
    score = np.exp(detections_final)/np.sum(np.exp(detections_final))
    label = labels[np.argmax(score)]
    return np.max(score), label

st.title("OpenCV Image Classification")

img = st.file_uploader("Upload Image",['jpeg','jpg','png'])

if img is not None:
    #Reading the image in bytes then converting into bytesarray and numpy array
    bytes_data = np.asarray(bytearray(img.read()),dtype='uint8')
    #Using OpenCV's imdecode funtion decodes numpy bytes array into image array in BGR sequence
    decoded = cv2.imdecode(bytes_data,cv2.IMREAD_COLOR)
    st.image(decoded[:,:,::-1])
    blob = cv2.dnn.blobFromImage(decoded, 0.017, (224,224), [104,117,124], swapRB=False,crop=False)
    net.setInput(blob)
    detections = net.forward()
    score, label = get_score_probability(detections)
    st.markdown('<div style= background-color:orange><b>Confidence: {score:.2f}<b>&nbsp;&nbsp;<b>Label: {label}</b></div>'.format(score=score * 100,label=label),unsafe_allow_html=True)