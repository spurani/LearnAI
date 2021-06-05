# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:21:36 2020

@author: SP
"""
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data = pd.read_csv("run_or_walk.csv")
data = data.drop(['date','time','username'],axis = 1)

y = data["activity"]
X = data.loc[:,data.columns != 'activity']

gnb = GaussianNB()
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3)
y_pred_gnb = gnb.fit(train_X,train_y).predict(test_X)

print("----------------------------------------------------------------")
print("Number of mislabelled points out of total of %d points: %d" %(data.shape[0],(test_y != y_pred_gnb).sum()))
print("Accuracy: ",((data.shape[0] - ((test_y != y_pred_gnb).sum())) / data.shape[0]))
print("Classification Report: \n",classification_report(y_pred_gnb,test_y))
print("----------------------------------------------------------------")

print("Acceleration values as Predictors")
y = data["activity"]
X = data.iloc[:,5:8]

gnb = GaussianNB()
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3)
y_pred_gnb = gnb.fit(train_X,train_y).predict(test_X)

print("----------------------------------------------------------------")
print("Number of mislabelled points out of total of %d points: %d" %(data.shape[0],(test_y != y_pred_gnb).sum()))
print("Accuracy: ",((data.shape[0] - ((test_y != y_pred_gnb).sum())) / data.shape[0]))
print("Classification Report: \n",classification_report(y_pred_gnb,test_y))
print("----------------------------------------------------------------")

print("Gyro values as Predictors")
y = data["activity"]
X = data.loc[:,['gyro_x','gyro_y','gyro_z']]

gnb = GaussianNB()
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3)
y_pred_gnb = gnb.fit(train_X,train_y).predict(test_X)

print("----------------------------------------------------------------")
print("Number of mislabelled points out of total of %d points: %d" %(data.shape[0],(test_y != y_pred_gnb).sum()))
print("Accuracy: ",((data.shape[0] - ((test_y != y_pred_gnb).sum())) / data.shape[0]))
print("Classification Report: \n",classification_report(y_pred_gnb,test_y))
print("----------------------------------------------------------------")
