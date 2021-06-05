# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:43:51 2020

@author: SP
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("voice-classification.csv")
print(data.isnull().sum())
corr = data.corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr, cbar = True,  square = True, cmap= 'coolwarm')
sns.countplot(data['label'],label = "Count")
X = data.iloc[:, :-1]
y = data.iloc[:,-1:]
gender_encoder = LabelEncoder()
y = gender_encoder.fit_transform(y)
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

logistic = LogisticRegression()
logistic.fit(X_train,y_train)
predict = logistic.predict(X_test)
print(accuracy_score(predict,y_test))
print(confusion_matrix(y_test,predict))
print(classification_report(y_test,predict))