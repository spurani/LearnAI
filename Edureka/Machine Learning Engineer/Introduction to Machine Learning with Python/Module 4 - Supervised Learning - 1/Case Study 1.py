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


X_train_new = X_train.drop(['skew','kurt','maxdom','dfrange'],axis=1)
X_test_new = X_test.drop(['skew','kurt','maxdom','dfrange'],axis=1)
pipeline.fit(X_train_new, y_train)
preds = pipeline.predict(X_test_new)
print(accuracy_score(preds, y_test))
print(confusion_matrix(y_test, preds))
print(classification_report(y_test, preds))
