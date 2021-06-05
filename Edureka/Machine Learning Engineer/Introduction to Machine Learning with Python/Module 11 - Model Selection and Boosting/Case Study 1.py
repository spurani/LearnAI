# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:26:05 2020

@author: SP
"""
import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("bio-degradabale-data.csv", sep=";", header = None)
array = df.values
X = array[:,1:-1]
Y = array[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
kfold = model_selection.KFold(n_splits=10, random_state=7, shuffle=True)
abc = AdaBoostClassifier(n_estimators=30, random_state=7)
results = model_selection.cross_val_score(abc, X, Y, cv=kfold)
print("Accuracy: ",results.mean())