# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:29:21 2020

@author: SP
"""

import csv
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

Salary = []
Gender = []
Age = []
PhD = []
with open("775_m5_datasets_v1.0/SalaryGender.csv") as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        Salary = np.append(Salary,row[0])
        Gender = np.append(Gender,row[1])
        Age = np.append(Age,row[2])
        PhD = np.append(PhD,row[3])

table = pd.read_csv("775_m5_datasets_v1.0/SalaryGender.csv")
men_with_phD = table.loc[(table['Gender'] == 1) & (table['PhD'] == 1)]
#print(men_with_phD)

women_with_phD = table.loc[(table['Gender'] == 0) & (table['PhD'] == 1)]
#rint(women_with_phD)

Age_df = pd.DataFrame(table['Age'])
PhD_df = pd.DataFrame(table['PhD'])
table1 = pd.concat([Age_df,PhD_df],axis=1)
#print(table1)

for i in table.index:
    if(table.loc[i]["PhD"] == 0):
        table = table.drop(i)

#print(table)

ar = [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]

dic = dict()
for i in ar:
    if(i in dic):
        dic[i] += 1
    else:
        dic[i] = 1
            
# print(dic)

fr = [None] * len(ar);  
visited = -1;  
   
for i in range(0, len(ar)):  
    count = 1;  
    for j in range(i+1, len(ar)):  
        if(ar[i] == ar[j]):  
            count = count + 1;  
            #To avoid counting same element again  
            fr[j] = visited;  
              
    if(fr[i] != visited):  
        fr[i] = count;  
   
#Displays the frequency of each element present in array  
# print("---------------------");  
# print(" Element | Frequency");  
# print("---------------------");  
# for i in range(0, len(fr)):  
#     if(fr[i] != visited):  
#         print("    " + str(ar[i]) + "    |    " + str(fr[i]));  
# print("---------------------");

q_six = np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9, 10, 11]])
filter_q_six = q_six > 5
new_arr = q_six[filter_q_six]
#print(new_arr)

q_seven = np.array([ np.nan,   1.,   2.,  np.nan,   3.,   4.,   5.])
#print(q_seven[~np.isnan(q_seven)])

q_eight = np.random.rand(10,10)
# print(q_eight)
# print(q_eight.min())
# print(q_eight.max())

q_nine = np.random.random(30)
#print(q_nine.mean())

q_ten = np.arange(11)
q_ten[(q_ten > 3) & (q_ten < 9)] *= -1
#print(q_ten)

q_eleven = np.random.rand(3,3)
q_eleven_ans = q_eleven[np.argsort(q_eleven[:,1])]
#print(q_eleven_ans)

q_twelve = np.random.rand(4,4)
#print(q_twelve)
#print(q_twelve[2]+q_twelve[3])

# q_thirteen = np.random.rand(4,4)
# print(q_thirteen)
# print(np.swapaxes(q_thirteen,-1))

q_fourteen = np.random.rand(3,3) 
#print(q_fourteen)
#print(np.linalg.matrix_rank(q_fourteen))

q_fifteen = pd.read_csv("775_m5_datasets_v1.0/middle_tn_schools.csv")
print("--------------------------------------------------------------------")
#print(q_fifteen.describe())
print("--------------------------------------------------------------------")
#print((len(q_fifteen.index)))
print("--------------------------------------------------------------------")
#print(q_fifteen.shape)
print("--------------------------------------------------------------------")
#print(q_fifteen.dtypes)
print("--------------------------------------------------------------------")
#print(q_fifteen.sum())
print("--------------------------------------------------------------------")
#print(q_fifteen.isnull().sum())
#print(q_fifteen.isnull().sum().sum())
print("--------------------------------------------------------------------")

q_school_rating = q_fifteen.groupby('school_rating').describe()
#print(q_school_rating)

plt.figure(figsize=(4,4))
selected_data =pd.DataFrame(pd.read_csv("775_m5_datasets_v1.0/middle_tn_schools.csv").loc[:,['name','school_rating','reduced_lunch']])
corr = selected_data.corr()
#print(corr)

x = np.array(selected_data["reduced_lunch"])
y = np.array(selected_data["school_rating"])
plt.scatter(x,y)
plt.title("The relationship between School Rating and Reduced Lunch")
plt.xlabel("Reduced Lunch")
plt.ylabel("School Rating")
#plt.show()

sn.heatmap(corr, annot=True)
plt.show()

