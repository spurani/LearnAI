# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 20:34:53 2020

@author: SP
"""

import pandas as pd
table1 = pd.read_csv("775_m5_datasets_v1.0/DSScoreTerm1.csv")
table2 = pd.read_csv("775_m5_datasets_v1.0/MathScoreTerm1.csv")
table3 = pd.read_csv("775_m5_datasets_v1.0/PhysicsScoreTerm1.csv")

#print(table1)
print("----------------")
#print(table2)
print("----------------")
#print(table3)
print("----------------")

del table1['Name']
del table2['Name']
del table3['Name']

print(table1['Ethinicity'].unique())
print(table2['Ethinicity'].unique())
print(table3['Ethinicity'].unique())


table1.loc[(table1['Ethinicity'] == 'White American'),'Ethinicity']=1
table1.loc[(table1['Ethinicity'] == 'European American'),'Ethinicity']=2
table1.loc[(table1['Ethinicity'] == 'Hispanic'),'Ethinicity']=3
table1.loc[(table1['Ethinicity'] == 'African American'),'Ethinicity']=4

table2.loc[(table2['Ethinicity'] == 'White American'),'Ethinicity']=1
table2.loc[(table2['Ethinicity'] == 'European American'),'Ethinicity']=2
table2.loc[(table2['Ethinicity'] == 'Hispanic'),'Ethinicity']=3
table2.loc[(table2['Ethinicity'] == 'African American'),'Ethinicity']=4

table3.loc[(table3['Ethinicity'] == 'White American'),'Ethinicity']=1
table3.loc[(table3['Ethinicity'] == 'European American'),'Ethinicity']=2
table3.loc[(table3['Ethinicity'] == 'Hispanic'),'Ethinicity']=3
table3.loc[(table3['Ethinicity'] == 'African American'),'Ethinicity']=4

#print(table1)
print("----------------")
#print(table2)
print("----------------")
#print(table3)
print("----------------")

# del table1['Ethinicity']
# del table2['Ethinicity']
# del table3['Ethinicity']

#print(table1)
print("----------------")
#print(table2)
print("----------------")
#print(table3)
print("----------------")

#print(table1.isnull().sum())
print("----------------")
#print(table2.isnull().sum())
print("----------------")
#print(table3.isnull().sum())
print("----------------")

table1 = table1.fillna(0.0)
table2 = table2.fillna(0.0)
table3 = table3.fillna(0.0)

table1 = table1.fillna(table1['Score'].mean())
table2 = table2.fillna(table2['Score'].mean())
table3 = table3.fillna(table3['Score'].mean())

#print(table1.isnull().sum())
print("----------------")
#print(table2.isnull().sum())
print("----------------")
#print(table3.isnull().sum())
print("----------------")

scoreFinal = pd.concat([table1,table2,table3])
scoreFinal.loc[(scoreFinal['Sex'] == 'M'),'Sex']=1
scoreFinal.loc[(scoreFinal['Sex'] == 'F'),'Sex']=2
#scoreFinal.to_csv("775_m5_datasets_v1.0/scorefinal_copy.csv")