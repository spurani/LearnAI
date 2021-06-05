# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:32:43 2021

@author: SP
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, roc_curve
from matplotlib import pyplot as plt

def randomdatasplitter(path):
    data = pd.read_csv(path)
    first = data.sample(frac=0.6)
    first.to_csv("First.csv",index=False)
    second = data.drop(first.index)
    second.to_csv("Second.csv",index=False)

#randomdatasplitter("698_m5_datasets_v1.0/HouseData.csv")

def labelencoder(path):
    data = pd.read_csv(path)
    label_encoder = preprocessing.LabelEncoder()
    data['Label'] = label_encoder.fit_transform(data['class'])
    data.to_csv("Marketing.csv",index=False)

#labelencoder("698_m5_datasets_v1.0/Marketing.csv")

def confusionmatrix(path):
    data = pd.read_csv(path)
    print(accuracy_score(data['ActualValues'],data['PredictedValues']))
    print(precision_score(data['ActualValues'],data['PredictedValues']))
    print(confusion_matrix(data['ActualValues'],data['PredictedValues']))
    print(recall_score(data['ActualValues'],data['PredictedValues']))
    fpr, tpr, ths = roc_curve(data['ActualValues'],data['PredictedValues'])
    plt.plot(fpr, tpr)
confusionmatrix("698_m5_datasets_v1.0/Results.csv")