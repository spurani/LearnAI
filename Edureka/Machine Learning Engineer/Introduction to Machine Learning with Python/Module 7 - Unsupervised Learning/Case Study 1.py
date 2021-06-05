# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 02:19:12 2020

@author: SP
"""
import numpy as np
import seaborn as sns
sns.set()
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')
data = pd.read_csv('driver-data.csv')
data = data.iloc[:,1:]

kmeans = KMeans(n_clusters = 5)
kmeans.fit(data)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
print(len(kmeans.labels_))
print(type(kmeans.labels_))
unique, counts = np.unique(kmeans.labels_, return_counts=True)
print(dict(zip(unique, counts)))
data['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
sns.lmplot('mean_dist_day','mean_over_speed_perc', data=data, hue='cluster',palette='coolwarm',size=6,aspect=1,fit_reg=False)