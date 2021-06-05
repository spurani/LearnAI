# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 01:25:04 2020

@author: SP
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

table = pd.read_csv("cereal.csv")

###
'''
For plotting the graphs please unccomment plots one by one for individual graphs 
as it will overlap in spyder if ran all the plots at once
'''
###

##Uncomment one by one
#plt.hist(table['sugars'])
#plt.hist(table['vitamins'])

table1 = table
table1["Manufacturer"] = table['mfr']
table1.loc[table1["Manufacturer"] == "N","Manufacturer"] = "Nabisco"
table1.loc[table1["Manufacturer"] == "Q","Manufacturer"] = "Quaker Oats"
table1.loc[table1["Manufacturer"] == "K","Manufacturer"] = "Kelloggs"
table1.loc[table1["Manufacturer"] == "R","Manufacturer"] = "Raslston Purina"
table1.loc[table1["Manufacturer"] == "G","Manufacturer"] = "General Mills"
table1.loc[table1["Manufacturer"] == "P","Manufacturer"] = "Post"
table1.loc[table1["Manufacturer"] == "A","Manufacturer"] = "American Home Foods Products"

#Uncomment
#table1['Manufacturer'].value_counts().plot.bar()

y = table1['rating']
x = table1.iloc[:,3:15]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 5)

lm = LinearRegression()
model = lm.fit(x_train,y_train)
pred_y = lm.predict(x_test)
print('Coefficients: \n', lm.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, pred_y))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, pred_y))

# Plot outputs
plt.scatter(y_test,pred_y,  color='black')
plt.plot(y_test, pred_y, color='blue', linewidth=3)
plt.xlabel("Y Test")
plt.ylabel("Predictor Y")
