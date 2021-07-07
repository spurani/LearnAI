# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:22:39 2021

@author: SP
"""

import cv2
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i",required=True,help="path to image",dest="bar")
args=vars(ap.parse_args())
print(args["bar"])