# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 08:16:15 2020

@author: SP
"""
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.decomposition import PCA
import pandas as pd

digits = load_digits()
print(digits.data.shape)

plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(digits.data[0:5], digits.target[0:5])):
  plt.subplot(1, 5, index + 1)
  plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
  plt.title('Training: %i\n' % label, fontsize = 20)
  
train_X, test_X, train_Y, test_Y = train_test_split(digits.data, digits.target, test_size = 0.2)

logistic = LogisticRegression()
logistic.fit(train_X,train_Y)
predict = logistic.predict(test_X)
print(accuracy_score(predict,test_Y))

X_digits, y_digits = digits.data, digits.target
pca = PCA(n_components=0.95)
fitter = pca.fit(X_digits)
reduced_data_pca = pca.transform(X_digits)
print(pca.explained_variance_ratio_)

pca.fit(X_digits)
existing_2d = pca.transform(X_digits)

train_X, test_X, train_Y, test_Y = train_test_split(existing_2d, digits.target, test_size = 0.2)
logistic = LogisticRegression()
logistic.fit(train_X,train_Y)
predict = logistic.predict(test_X)
print(accuracy_score(predict,test_Y))

print(confusion_matrix(predict,test_Y))
final = pd.DataFrame({'test':test_Y,'predict':predict})
final[final['test'] != final['predict']]

print(final[final['test'] != final['predict']].index)
for i in final[final['test'] != final['predict']].index:
    print("Target: ",digits.target[i],end='\n-----------------\n')
    plt.imshow(digits.images[i],cmap=plt.cm.gray)
    print("Predicted: ",final.loc[i,'predict'],end='\n-----------------\n')