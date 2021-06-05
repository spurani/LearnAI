# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 03:03:27 2020

@author: SP
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#table = pd.read_csv("775_m6_datasets_v1.0/Hurricanes.csv")
#plt.bar(table['Year'],table['Hurricanes'])
#plt.xlabel("Year")
#plt.ylabel("Number of Hurricanes")
#plt.title("Number of Hurricanes per year")

# table1 = pd.read_csv("775_m6_datasets_v1.0/CityTemps.csv")
# data = table1.loc[(table1['Year'] == 2014) | (table1['Year'] == 2015),('San Francisco','Moscow')]
# plt.hist(data)
# plt.grid(True)
# plt.ylabel("Times")
# plt.xlabel("Temperature")
# plt.title("Temperature of San Francisco and Moscow")

plt.figure(figsize=(100,100))
table2 = pd.read_csv("775_m6_datasets_v1.0/Cars2015.csv")
table2['count'] = table2.groupby('Make')['Make'].transform('count')
table2.drop_duplicates('Make',inplace = True)
table2.sort_values(by='count',ascending=False,inplace=True)
ax1 = plt.subplot(121, aspect='equal')
table2.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%',startangle=90, shadow=False, labels=table2['Make'], legend = False, fontsize=10) 

# table3 = pd.read_csv("775_m6_datasets_v1.0/sample-salesv2.csv")
# #print(table3['unit price'].describe())

# df = pd.DataFrame(table3,columns=['name','net_price','date']) 
# df2 = df.groupby("name").groups

# sales = df.groupby("name").sum()
# sales.sort_values(by='net_price',ascending=False).plot(kind='bar',legend=None,title="Total Sales by Customer")
