# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 22:05:58 2020

@author: SP
"""
import pandas as pd
import sys
data = pd.read_csv("651_m3_datasets_v1.0/bank-data.csv")
jobs = set(data['job'])
print(jobs)
print(sys.argv[1])
print("Max Age: ",data['age'].max())
print("Min Age: ",data['age'].min())
if(sys.argv[1].lower() in jobs):
           if(sys.argv[1].lower() in jobs):
               print("Profession found")
           else:
               print("not found")
a = 0
while(True):
    user = input("Please enter profession: ")
    if(user != "END"):
         if(user in jobs):
             print("Profession found")
         else:
            print("not found")
    if(user == "END"):
        break
age = {'max': 80,'min': 19}
