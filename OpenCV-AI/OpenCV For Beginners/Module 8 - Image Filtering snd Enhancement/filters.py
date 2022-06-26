import cv2
import numpy as np

def black_and_white(img):
    filtered = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return filtered

def sepia(img):
    img_sepia = img.copy()
    # Converting to RGB as sepia matrix below is for RGB
    img_sepia = cv2.cvtColor(img_sepia,cv2.COLOR_BGR2RGB)
    img_sepia = img_sepia.astype('float64')
    img_sepia = cv2.transform(img_sepia, np.matrix([
        [0.393, 0.769, 0.189],[0.349, 0.686, 0.168],[0.272, 0.534, 0.131]
    ]))
    # Clip values to the range [0,255]
    img_sepia = np.clip(img_sepia, 0, 255)
    img_sepia = img_sepia.astype('uint8')
    img_sepia = cv2.cvtColor(img_sepia,cv2.COLOR_RGB2BGR)
    return img_sepia

def vignette(img, level):
    height, width = img.shape[:2]
    # Generate vignette mask using Gaussian Kernel.
    X_resultant_kernel = cv2.getGaussianKernel(width,width/level)
    Y_resultant_kernel = cv2.getGaussianKernel(height,height/level)
    # Generating resultant_kernel matrix.
    kernel = Y_resultant_kernel * X_resultant_kernel.T
    mask = kernel / kernel.max()
    img_vignette = img.copy()
    # Applying the mask to each channel in the input image
    for i in range(3):
        img_vignette[:,:,i] = img_vignette[:,:,i] * mask
    return img_vignette

def pencil_sketch(img,ksize):
    img_blur = cv2.GaussianBlur(img,(ksize,ksize),0)
    pencilsketch,_ = cv2.pencilSketch(img_blur)
    return pencilsketch