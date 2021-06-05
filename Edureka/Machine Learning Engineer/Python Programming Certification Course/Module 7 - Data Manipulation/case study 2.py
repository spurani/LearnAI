# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 06:39:25 2020

@author: SP
"""

import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv("775_m7_datasets_v1.0/Salaries.csv")
# print(table.shape)
# print(table.isnull().sum())
# print(table.isnull().sum().sum())
# print(table.dtypes)
# print(table)
# q1 = table.loc[(table["Year"] == 2011) | (table['Year'] == 2014),'TotalPayBenefits'].mean()
# print(q1)

# q2 = table.groupby(['JobTitle','Year']).mean()['TotalPay'].max()
# print(q2)

# q3 = table.loc[table['Year'] == 2014,'OvertimePay'].mean()
# print(q3)

#q4 = table.loc[table['Year'] == 2014,'JobTitle'].value_counts().head()
#print(q4)

#q5 = table.groupby('Year')['TotalPay','EmployeeName'].max()
#print(q5)

#q6 = table.loc[table['Year'] == 2014,'JobTitle'].value_counts().tail()
#print(q6)

# q7 = table.groupby(['JobTitle','Year']).mean()['TotalPay'].min()
# print(q7)

q8 = table.loc[table['Year']==2014,['OvertimePay','TotalPayBenefits']]
print(q8.corr())
print(q8)