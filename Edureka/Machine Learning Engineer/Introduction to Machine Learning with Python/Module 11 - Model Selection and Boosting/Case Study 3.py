# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:07:41 2020

@author: SP
"""
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

data = pd.read_csv("letterCG.bin", sep=" ")
data = pd.DataFrame(data)
new_data = data.dropna(axis = 1)

x = new_data.iloc[:,1:-1]
y = new_data.loc[:,'Class']
train_X, test_X, train_Y, test_Y = train_test_split(x,y, test_size = 0.3 )
decisionTreeClassifier = DecisionTreeClassifier(max_depth=1,)
estimator_array = range(1,17)

for i in estimator_array:
    abc = AdaBoostClassifier(base_estimator=decisionTreeClassifier, n_estimators=i)
    model = abc.fit(train_X, train_Y)
    print("Accuracy: ",cross_val_score(model,x,y).mean()," ", abc.n_estimators)
