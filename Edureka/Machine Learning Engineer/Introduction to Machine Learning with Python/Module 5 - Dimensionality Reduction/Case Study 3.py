# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:23:51 2020

@author: SP
"""

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data = pd.read_csv("breast-cancer-data.csv")
data = data.drop('id',axis=1)
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), ['diagnosis'])])
pipeline = Pipeline(steps=[('feature_engineer', columnTransformer),('PCA', PCA(n_components=2))])
pipeline.fit(data)
data_new = pipeline.transform(data)
print(data_new)
X_train, X_test, y_train, y_test = train_test_split(data_new,data['diagnosis'],test_size = 0.2)
logistic = LogisticRegression()
logistic.fit(X_train,y_train)
predict = logistic.predict(X_test)
print(accuracy_score(predict,y_test))
print(confusion_matrix(y_test, predict))
print(classification_report(y_test, predict))
