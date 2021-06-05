# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:23:43 2020

@author: SP
"""
import sys
fo = open("bank-data.csv") 
reader = fo.readlines()
dict = {}
myset = set()
age = set()

for i in reader:
     whole_string = i
     splitter = i.split(",")
     dict.setdefault(splitter[1],whole_string) 
     if(splitter[0] != "age"):
         age.add(splitter[0])
     
for i in dict:
    myset.add(i)
list_set = list(myset)

if(str(sys.argv[1]) != "" ):
        if(str(sys.argv[1]).lower() in list_set):
            print("Profession exists")
        else:
            print("Profession does not exists")
            
while True:
        job = input("Please enter profession: ")
        if(job in list_set):
            print("Profession exists")
        if(job not in list_set):
            print("Profession does not exists")
        if(job == "END"):
                break

max_age = int(max(age))
min_age = int(min(age))

min_max = {'min_age':min_age,'max_age':max_age}
print(min_max)
#second method        
# fo = open("bank-data.csv")
# professions = []
# for row in fo:
#     professions.append(row.split(',')[1])
# unique_professions = list(set(professions))
# unique_professions