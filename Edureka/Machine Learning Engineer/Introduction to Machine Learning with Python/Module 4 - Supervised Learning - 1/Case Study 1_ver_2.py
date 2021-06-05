# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 03:28:09 2020

@author: SP
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 04:02:32 2020

@author: SP
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.pipeline import Pipeline

table = pd.read_csv("voice.csv")
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), ['label'])])
#ct = np.array(columnTransformer.fit_transform(table), dtype = np.str)
X_train, X_test, y_train, y_test = train_test_split(table,table['label'],test_size = 0.2)
print(X_train.shape)
print(X_test.shape)
pipeline = Pipeline(steps=[('feature_engineer', columnTransformer),('LR', LogisticRegression())])
pipeline.fit(X_train, y_train)
preds = pipeline.predict(X_test)
print(accuracy_score(preds, y_test))
print(confusion_matrix(y_test, preds))
print(classification_report(y_test, preds))




#----------------------------WORKING------------------
# train,test = train_test_split(table,test_size = 0.2)
# #print(train.shape)
# #print(test.shape)
# prediction_var = ['median','Q25','Q75','IQR','skew','kurt','spent','sfm','mode','centroid','meanfun','minfun','maxfun','meandom','mindom','maxdom','dfrange','modindx']
# #print(prediction_var)
# train_X = train[prediction_var]
# train_Y  = train.label
# #print(train.label)
# test_X = train[prediction_var]
# test_Y  = train.label
# logisticregression = LogisticRegression()
# lr = logisticregression.fit(train_X,train_Y)
# predict = logisticregression.predict(test_X)
# accuracy = accuracy_score(predict,test_Y)
# print(accuracy)

# sn.heatmap(train_X.corr())
# print(train_X.corr())

#plt.figure(figsize=(25, 25))
#sn.heatmap(X_train.corr(),annot=True)
# print(X_train.corr())

X_train_new = X_train.drop(['skew','kurt','maxdom','dfrange'],axis=1)
X_test_new = X_test.drop(['skew','kurt','maxdom','dfrange'],axis=1)
pipeline.fit(X_train_new, y_train)
preds = pipeline.predict(X_test_new)
print(accuracy_score(preds, y_test))
print(confusion_matrix(y_test, preds))
print(classification_report(y_test, preds))

#----------------------------WORKING------------------
# prediction_var = ['median','Q25','Q75','IQR','spent','sfm','mode','centroid','meanfun','minfun','maxfun','meandom','mindom','modindx']
# #print(prediction_var)
# train_X = train[prediction_var]
# train_Y  = train.label
# #print(train.label)
# test_X = train[prediction_var]
# test_Y  = train.label
# logisticregression = LogisticRegression()
# lr = logisticregression.fit(train_X,train_Y)
# predict = logisticregression.predict(test_X)
# accuracy = accuracy_score(predict,test_Y)
# print(accuracy)
