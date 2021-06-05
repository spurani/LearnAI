# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:21:41 2020

@author: SP
"""
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("glass.csv")
plotter = data['Type'].value_counts().plot(kind='bar')
train, test = train_test_split(data, test_size= 0.3)
train_X = train.iloc[:,0:-1]
test_X = test.iloc[:,0:-1]
train_Y = train['Type']
test_Y = test['Type']
DecisionTreeClassifier = DecisionTreeClassifier()
model = DecisionTreeClassifier.fit(train_X,train_Y)
y_pred = model.predict(test_X)
Kfold = KFold(n_splits=3)
model_kfold = Kfold.split(model)
print(accuracy_score(test_Y,y_pred))
print(classification_report(test_Y,y_pred))
grid_values = {'n_estimators':[1, 10, 100, 500, 1000]}
grid_clf_acc = GridSearchCV(RandomForestClassifier(), param_grid = grid_values, cv = 10)
grid_clf_acc.fit(train_X,train_Y)
predict = grid_clf_acc.predict(test_X)
print("---------------------------------------------")
print("--------- RandomForestClassifier Model---------------")
print("Accuracy: ",accuracy_score(predict,test_Y))
print("Confusion Matrix: \n",confusion_matrix(predict,test_Y))
print("Classification Report: \n",classification_report(predict,test_Y))
# print best parameter after tuning 
print("Best Hyperparameter: ",grid_clf_acc.best_params_)
print("Best Estimator: ",grid_clf_acc.best_estimator_)