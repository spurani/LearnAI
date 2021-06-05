# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 02:15:25 2020

@author: SP
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = pd.read_csv("loan_borowwer_data.csv")
data.drop("purpose",axis=1,inplace=True)
corr = data.corr()
plt.figure(figsize=(20,20))
sns.heatmap(corr,cbar = True, square = True, cmap = 'coolwarm',annot=True)
sns.countplot(data['not.fully.paid'],label="Count")
train,test = train_test_split(data, test_size = 0.3)
print(train.shape)
print(test.shape)
train_X = train.iloc[:,:-1]
train_Y = train['not.fully.paid']
test_X = test.iloc[:,:-1]
test_Y = test['not.fully.paid']
logistic = LogisticRegression()
logistic.fit(train_X,train_Y)
temp = logistic.predict(test_X)
print(metrics.accuracy_score(temp, test_Y))