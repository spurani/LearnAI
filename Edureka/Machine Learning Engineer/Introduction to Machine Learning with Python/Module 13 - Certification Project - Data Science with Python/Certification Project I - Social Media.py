# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:13:15 2020

@author: SP
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import LocalOutlierFactor

data = pd.read_csv("OnlineNewsPopularity.csv")
print(data.isnull().sum())
print(data.isnull().sum().sum())
print(data.shape)
print(data.info())
x = data.iloc[:,1:-1]
y = data["shares"]
data = data.drop('url',axis=1)

coorelations = data.corr()
plt.figure(figsize=(50,50))
sns.heatmap(coorelations, square = True, cmap = 'YlGnBu', annot=True)
plt.yticks(rotation = 0)
plt.xticks(rotation = 90)
plt.show()

#load the dataset
#split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)

'''
LocalOutlierFactor for removing outliers (Automatic Outlier detection)
'''
lof = LocalOutlierFactor()
yhat = lof.fit_predict(X_train)
# select all rows that are not outliers
mask = (yhat != -1)
X_train, y_train = X_train.iloc[mask, :], y_train.iloc[mask]
# summarize the shape of the updated training dataset
print(X_train.shape, y_train.shape)
# fit the model
model = LinearRegression()
model.fit(X_train, y_train)
# evaluate the model
yhat = model.predict(X_test)

# evaluate predictions
mae = mean_absolute_error(y_test, yhat)
mse = mean_squared_error(yhat,y_test)
print('Linear Regression MAE: %.3f' % mae)
print('Linear Regression MSE: %.3f' % np.sqrt(mse))
plt.subplots(figsize=(15,10))
sns.regplot(x=y_test, y=yhat)
plt.show()

'''
Decision tree Regression
'''
model = DecisionTreeRegressor()
model.fit(X_train,y_train)# now fit our model for traiing data
prediction=model.predict(X_test)
mae = mean_absolute_error(y_test, yhat)
mse = mean_squared_error(yhat,y_test)
print('DeciSiontree Regression MAE: %.3f' % mae)
print('Decisiontree Regression MSE: %.3f' % np.sqrt(mse))