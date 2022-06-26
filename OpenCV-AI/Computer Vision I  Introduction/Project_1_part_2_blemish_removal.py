# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:05:19 2021

@author: SP
"""

import cv2
import numpy as np

def calculateVariance(patch):
    x = cv2.Scharr(patch, -1, 1, 0)
    y = cv2.Scharr(patch, -1, 0, 1)

    return np.abs(x) + np.abs(y)

def getPatch(xy, img):
    patch = img[xy[1] - 15:xy[1] + 15, xy[0] - 15:xy[0] + 15]
    return patch

def pickBestAround(xy, values, image):
    bestV = 0
    best_xy = None
    for move in np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]) * 30:
        xy_m = xy + move
        if xy_m[xy_m<0].sum() < 0:
            continue
        patch = getPatch(xy_m, values)
        variance = 1/calculateVariance(patch).sum()
        if variance > bestV:
            bestV = variance
            best_xy = xy_m

        return getPatch(best_xy, values), getPatch(best_xy, image)

def onMouseCallback(action, x, y, flags, img):
    if action == cv2.EVENT_LBUTTONDOWN or action == cv2.EVENT_RBUTTONDOWN:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[:, :, 0]
        (grayPatch, colorPatch) = pickBestAround((x, y), gray, img)
        src_mask = np.ones_like(grayPatch) * 255
        cv2.seamlessClone(
            colorPatch, img, src_mask, (x, y), cv2.NORMAL_CLONE, blend=img)

img = cv2.imread("blemish.png", 1)
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", onMouseCallback, img)

k = 0
while k != 27:
    cv2.imshow("Window", img)
    k = cv2.waitKey(20)

cv2.destroyAllWindows()