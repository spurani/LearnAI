# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:43:40 2020

@author: SP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

table = pd.read_csv("prisoners.csv")

'''
1.Data Loading:a.Load the dataset “prisoners.csv” using pandas and display 
the first and last five rows in the dataset. 
[Hint: Refer to read_csv,head and tail methods in pandas]
'''
print(table.head())
print(table.tail())

'''
b.Use describe method in pandas and find out the number of columns. 
Can you say something about those rows who have zero inmates?
[Hint: Use the loc attribute of dataframe combined with conditional checks]
'''
print(table.describe())
table1 = table.loc[(table['No. of Inmates benefitted by Elementary Education'] == 0) | (table['No. of Inmates benefitted by Adult Education'] == 0) | (table['No. of Inmates benefitted by Higher Education'] == 0) | (table['No. of Inmates benefitted by Computer Course'] == 0)]
print(table1)

'''
2.Data Manipulation:a.Create a new column -’total_benefitted’ that is a sum of 
inmates benefitted through all modes.[Hint: Use sum method with appropriate axis]
'''
table2 = table
table2['total benefitted'] = table2[['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education','No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course']].sum(axis=1)
print(table2)

'''
b.Create a new row -“totals” that is the sum of all inmates benefitted 
through each mode across all states.
'''
table2.loc['totals',2:] = table2.sum(axis=0)
print(table2)

'''
3.Plotting:
a.Make a bar plot with each state name on the x -axis and their total benefitted inmates as their bar heights.
Which state has the maximum number of beneficiaries?
[Hint: Use bar method of pyplot]
'''
table4 = table2
table4 = table4.drop('totals')
table4 = table4.loc[table4['total benefitted'] != 0]
xlabels = table4['STATE/UT'].values
plt.figure(figsize=(20, 3))
plt.xticks(np.arange(xlabels.shape[0]), xlabels, rotation = 'vertical', fontsize = 18)
plt.xticks
plt.bar(np.arange(table4.values.shape[0]),table4['total benefitted'],align = 'edge')
'''
b.Make a pie chart that depicts the ratio among different modes of benefits.
[Hint: Use pie method of pyplot]
'''
table3 = table2
table3 = table2.loc[table2['total benefitted'] != 0]
table3 = table3.drop('totals')
colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]
plt.pie(table3['total benefitted'],# with no shadows
    shadow=False,
    labels=table3['STATE/UT'],
    # with colors
    colors=colors,
    autopct='%1.1f%%',
    startangle=90
    )