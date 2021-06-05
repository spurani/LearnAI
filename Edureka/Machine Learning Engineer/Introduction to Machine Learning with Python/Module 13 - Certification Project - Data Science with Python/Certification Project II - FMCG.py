# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:47:26 2020

@author: SP
"""
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import seaborn as sns

data = pd.read_csv("Project_Data_2.csv", index_col=0, thousands=',')
data = pd.DataFrame(data)
data.index.names = ['Country']
data.columns.names = ['Year']
#print(data.isnull().sum())
pca = PCA(n_components=2)
pca.fit(data)
data_2d = pca.transform(data)
data_df_2d = pd.DataFrame(data_2d)
data_df_2d.index = data.index
data_df_2d.columns = ['PC1', 'PC2']
features = range(pca.n_components)
print(pca.explained_variance_ratio_)

ax = data_df_2d.plot(kind='scatter', x='PC2', y='PC1', figsize=(16,8))
for i, country in enumerate(data.index):
    ax.annotate(country, (data_df_2d.iloc[i].PC2, data_df_2d.iloc[i].PC1))
plt.bar(features, pca.explained_variance_ratio_, color='black')
plt.xlabel('PCA features')
plt.ylabel('variance %')
plt.xticks(features)
ks = range(1,10)
inertias = []
for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(data_df_2d)
    inertias.append(model.inertia_)
# plt.plot(ks,inertias,'-o',color='black')
# plt.xlabel('number of clusters, k')
# plt.ylabel('inertia')
# plt.xticks(ks)

plt.rcParams['figure.figsize'] = (5,5)
plt.style.use('ggplot')
f1 = data_df_2d['PC1'].values
f2 = data_df_2d['PC2'].values
X = np.array(list(zip(f1, f2)))
Z = linkage(X, 'ward')
#fig = plt.figure(figsize = (5,5))
#dn = dendrogram(Z)
z = linkage(X, 'single')
#fig = plt.figure(figsize = (10,5))
#dn = dendrogram(z)

kmeans = KMeans(n_clusters = 2)
kmeans.fit(data_df_2d)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
print(type(kmeans.labels_))
unique, counts = np.unique(kmeans.labels_,return_counts = True)
print(dict(zip(unique,counts)))
data_df_2d['cluster'] = kmeans.labels_
sns.set_style('whitegrid')
#sns.lmplot('PC2','PC1',data=data_df_2d,hue='cluster',palette='coolwarm',height=6,aspect=1,fit_reg=False)