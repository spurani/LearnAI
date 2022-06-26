import streamlit as st
import numpy as np
from filters import *
import cv2
st.title("Artistic Image Filters using Computer Vision")
img=st.file_uploader("Choose an image file:",['png','jpg','jpeg'])
if img is not None:
    raw_bytes = np.asarray(bytearray(img.read()),dtype='uint8')
    img = cv2.imdecode(raw_bytes,cv2.IMREAD_COLOR)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original")
        st.image(img,channels='BGR')
    st.header("Filter Examples:")
    selectedbox=st.selectbox("Select a filter:",["None","Black and White","Sepia/Vintage","Vignette Effect","Pencil Sketch"])
    filter_bw, filter_sepia, filter_vignette, filter_pencil_sketch = st.columns(4)
    with filter_bw:
        st.write('Black & White')
        st.image('filter_bw.jpg')
    with filter_sepia:
        st.write('Sepia/Vintage')
        st.image('filter_sepia.jpg')
    with filter_vignette:
        st.write('Vignette')
        st.image('filter_vignette.jpg')
    with filter_pencil_sketch:
        st.write('Pencil Sketch')
        st.image('filter_pencil_sketch.jpg')
    if selectedbox == "Black and White":
        filtered = black_and_white(img)
    if selectedbox == "Sepia/Vintage":
        filtered = sepia(img)[:,:,::-1]
    if selectedbox == "Vignette Effect":
        level = st.slider("Level:",2,7,5)
        filtered = vignette(img,level)[:,:,::-1]
    if selectedbox == "Pencil Sketch":
        ksize = st.slider('Blur Kernel Size',1,11,5,2)
        filtered = pencil_sketch(img,ksize)
    if selectedbox != 'None':
        with col2:
            st.title("Output")
            st.image(filtered)