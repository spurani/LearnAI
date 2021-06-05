# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:49:25 2020

@author: SP
"""
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import pandas as pd

digits = load_digits()
train_X, test_X, train_Y, test_Y = train_test_split(digits.data, digits.target, test_size = 0.2, train_size= 0.8)
lda = LDA(n_components=2)
lda.fit(train_X,train_Y)
lda.transform(train_X)
print(lda.explained_variance_ratio_)

X_digits, y_digits = digits.data, digits.target
lda = LDA(n_components=2)
lda.fit(X_digits,y_digits)
existing_2d = lda.transform(X_digits)

train_X, test_X, train_Y, test_Y = train_test_split(existing_2d, digits.target, test_size = 0.2, train_size= 0.8)
logistic = LogisticRegression()
logistic.fit(train_X,train_Y)
predict = logistic.predict(test_X)
print(accuracy_score(predict,test_Y))
print(confusion_matrix(predict,test_Y))