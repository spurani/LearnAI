# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 03:01:50 2020

@author: SP
"""
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

im = Image.open("dogs.jpeg")
#im.show()
im_array = np.array(im)
print(im_array)
print(im_array.ndim)
print(im_array.shape)
x, y, z = im_array.shape
im_array_2d = np.reshape(im_array,(x*y,z))
print(im_array_2d)
print(im_array_2d.ndim)
print(im_array_2d.shape)

kmeans = KMeans(n_clusters = 3)
kmeans.fit(im_array_2d)
print(kmeans.labels_)
print(kmeans.cluster_centers_)
print(len(kmeans.labels_))
print(type(kmeans.labels_))
unique, counts = np.unique(kmeans.labels_,return_counts=True)
print(dict(zip(unique,counts)))
plt.figure(figsize = (16,9))
plt.imshow(((kmeans.cluster_centers_[kmeans.labels_].reshape(x,y,z)) * 255).astype(np.uint8))

r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
ax = Axes3D(plt.figure(figsize = (16,9)))
ax.scatter(r, g, b)
plt.scatter(r,g,b)