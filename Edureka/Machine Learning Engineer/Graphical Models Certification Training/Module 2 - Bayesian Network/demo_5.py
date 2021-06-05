# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:05:56 2020

@author: SP
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from pgmpy.base import DAG
import networkx as nx
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
label_encoder = preprocessing.LabelEncoder() 
data = pd.read_csv("779_m2_demo_5/PimaIndians.csv")
data['test']= label_encoder.fit_transform(data['test'])
x = data.iloc[:,0:8]
y = data['test']
train_x, test_x, train_y, test_y = train_test_split(x,y,test_size=0.3)
model = LogisticRegression()
model.fit(train_x,train_y)
y_pred = model.predict(test_x)
print(accuracy_score(test_y, y_pred))
print(confusion_matrix(test_y, y_pred))
print(classification_report(test_y, y_pred))

g = DAG()
g.add_edges_from([('pregnant','test'),('glucose','test'),('diastolic','test'),('triceps','test'),('insulin','test'),('bmi','test'),('diabetes','test'),('age','test')])
nx.draw_networkx(g, with_labels=True)
sample_id = 12
y_test_sample = test_y.iloc[sample_id]
x_test_sample = test_x.iloc[sample_id,:].values.reshape(1,-1)
print(model.predict(x_test_sample.reshape(1,-1)))
print(model.predict_proba(x_test_sample))
print(model.coef_)
score=np.dot(model.coef_,x_test_sample[0])
def sigmoid(x):
 return 1 / (1 + np.exp(-x))
sigmoid(score)
print(sigmoid(model.intercept_ + score))
