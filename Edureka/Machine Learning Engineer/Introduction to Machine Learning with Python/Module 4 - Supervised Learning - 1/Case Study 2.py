# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:08:41 2020

@author: SP
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

table = pd.read_csv("horse.csv")
table = pd.get_dummies(table)

table = table.fillna(table.mode().iloc[0])
table = table.drop('hospital_number',axis=1)
train, test = train_test_split(table, test_size=0.3)
prediction_var = table[:].columns
train_X = train[prediction_var]
train_Y = train[['outcome_died', 'outcome_euthanized', 'outcome_lived']]
test_X = train[prediction_var]
test_Y = train[['outcome_died', 'outcome_euthanized', 'outcome_lived']]

model = tree.DecisionTreeClassifier()
model.fit(train_X,train_Y)
predict = model.predict(test_X)
print(accuracy_score(predict,test_Y))

model = RandomForestClassifier()
model.fit(train_X,train_Y)
predict = model.predict(test_X)
print(accuracy_score(predict,test_Y))
