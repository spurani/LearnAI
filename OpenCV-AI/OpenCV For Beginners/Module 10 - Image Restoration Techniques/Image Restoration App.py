import cv2
import numpy as np
import pathlib
import streamlit as st
from PIL import Image
import io
from streamlit_drawable_canvas import st_canvas
import base64

STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
DOWNLOADS_PATH = (STREAMLIT_STATIC_PATH / "downloads")
if not DOWNLOADS_PATH.is_dir():
    DOWNLOADS_PATH.mkdir()

def get_image_download_link(img, filename, text):
    """Generate a link to download a particular image file."""
    buffered = io.BytesIO()
    img.save(buffered,format='JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/txt;base64,{img_str}" downloads="{filename}">{text}</a>'
    return href

st.sidebar.title("Image Restoration Application using Image Inpainting with Computer Vision")
file = st.sidebar.file_uploader("Upload an image to restore:",["png","jpg",".jpeg"])
if file is not None:
    file_bytes = np.asarray(bytearray(file.read()),dtype='uint8')
    image = cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)##BGR
    stroke_width = st.sidebar.slider("Stroke width",1,25,5,5)
    h, w = image.shape[:2]
    if w > 800:
        h_, w_ = int(h * 800 / w), w
    else:
        h_, w_ = h, w
    canvas_result = st_canvas(
        fill_color='white',
        stroke_width=stroke_width,
        stroke_color='black',
        background_image=Image.open(file).resize((h_, w_)),
        update_streamlit=True,
        height=h_,
        width=w_,
        drawing_mode='freedraw',
        key='canvas'
    )
    stroke = canvas_result.image_data
    if stroke is not None:
        ck = st.sidebar.checkbox("Show mask")
        if(ck):
            st.image(stroke)
        mask = cv2.split(stroke)[3]
        mask = np.uint8(mask)
        mask = cv2.resize(mask,(w,h))
        st.sidebar.caption("Happy with selection?")
        option=st.sidebar.selectbox("Mode",["None","Naive Stokes","Telea","Compare both"])
        if(option == "Naive Stokes"):
            dst = cv2.inpaint(src=image,inpaintMask=mask,inpaintRadius=3,flags=cv2.INPAINT_NS)[:,:,::-1]
            st.image(dst)
            result_dst = Image.fromarray(dst)
            st.sidebar.markdown(get_image_download_link(result_dst,'downloaded.jpeg','Download Output'),unsafe_allow_html=True)
        elif(option == "Telea"):
            dst = cv2.inpaint(src=image,inpaintMask=mask,inpaintRadius=3,flags=cv2.INPAINT_TELEA)[:,:,::-1]
            st.image(dst)
            result_dst = Image.fromarray(dst)
            st.sidebar.markdown(get_image_download_link(result_dst,'downloaded.jpeg','Download Output'),unsafe_allow_html=True)
        elif(option == "Compare both"):
            dst_ns = cv2.inpaint(src=image,inpaintMask=mask,inpaintRadius=3,flags=cv2.INPAINT_NS)[:,:,::-1]
            dst_telea = cv2.inpaint(src=image,inpaintMask=mask,inpaintRadius=3,flags=cv2.INPAINT_TELEA)[:,:,::-1]
            ns, telea = st.columns(2)
            with ns:
                st.subheader("Result of Naive Stokes")
                st.image(dst_ns)
            with telea:
                st.subheader("Result of Telea")
                st.image(dst_telea)
            if(dst_ns is not None):
                result_dst_ns = Image.fromarray(dst_ns)
                st.sidebar.markdown(get_image_download_link(result_dst_ns,'ns.jpeg','Download Output of Naive Stokes'),unsafe_allow_html=True)
            if(dst_ns is not None):
                result_dst_telea = Image.fromarray(dst_ns)
                st.sidebar.markdown(get_image_download_link(result_dst_ns,'telea.jpeg','Download Output of Telea'),unsafe_allow_html=True)
        else:
            pass