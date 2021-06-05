# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:34:14 2020

@author: SP
"""
from pomegranate import *
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
data = pd.DataFrame(pd.read_csv('779_m2_demo_4/Iris.csv'))
x = data.iloc[:,1:5]
y = data.iloc[:,5]
train_X, test_X, train_Y, test_Y = train_test_split(x,y,test_size = 0.3)
model = GaussianNB()
model.fit(train_X, train_Y)
y_pred = model.predict(test_X)
print(accuracy_score(test_Y,y_pred))
print(confusion_matrix(test_Y,y_pred))
print(classification_report(test_Y,y_pred))
data = data.drop('Id',axis=1)
features = x.columns
print(features)
unique_vals = data['Species'].unique()  # [0, 1, 2]
#print(unique_vals)

d = data.groupby('Species')

for i in d:
        sns.distplot(i[1].iloc[:,0:4], hist=False, rug=True)

#for index, column in data.groupby():
    
    #sns.distplot(, hist=False, rug=True)
    #print(targets[i])

sns.pairplot(data, hue="Species", height = 2, palette = 'colorblind');

'''Normalisation working perfectly approach'''
# df = data.melt(['Species'], var_name='cols',  value_name='vals')
# #print(df)
# g = sns.FacetGrid(df, col='cols', hue="Species", palette="Set1")
# g = (g.map(sns.distplot, "vals", hist=False, rug=True))
# g.add_legend()