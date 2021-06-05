# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:24:17 2020

@author: SP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

#Dont forget to !!!!!!!! to change csv below!!!!!!!!
table = pd.read_csv('mew2ktykm4.csv',na_values = [])
####!!!!!!!!!!!!!###################################

# print(table.shape) ##Shapes gives information about number rows and coloumns respectively(r,c)
# print(table.dtypes) ##List all datatypes in dataframe

print("-----FIND NULL VALUES-----------")
#print(table.isnull().values.any())
print("-----SUM OF NULL VALUES---------")
#print(table.isnull().sum())
print("-----TOTAL SUM OF NULL VALUES---")
#print(table.isnull().sum().sum())
print("--------------------------------")
''' Compute -- What are the top 10 Zipcodes for 911 & 
Question 1: Are Zipcodes 19446 and 19090 present ?
'''

#table1 = table['zip'].dropna()
#zip_code = table1.value_counts().head(10)
# print(zip_code)

'''
Compute --What are the top 4 townships (twp) for 911 calls  
& Question 2: Which  of the following township are  not present? 
--LOWER POTTSGROVE, NORRISTOWN, HORSHAM, ABINGTON
'''

#table2 = table['twp'].dropna()
#twp = table2.value_counts().head(4)
# print(twp)

'''
Compute --Create new features & Question 3: What is the most common 
Reason for a 911 call based on Reason Column? Which comes second
'''

table3 = table
table3[['department','reason']] = table['title'].str.split(":",expand=True)
department = table3['department'].value_counts()
reason = table3['reason'].value_counts()
# print(department)
# print(reason)

'''
Compute --Plot barchart using matplot for 911 calls by Reason 
& Question 4: How can you plot the bars horizontally ?
'''

#department.plot(kind='barh',title="911 Calls By Reason",legend=True)

'''
Do data manipulation & Question 5: Which day got maximum calls 
for EMS and how many?
'''
ems_timestamp = table.loc[table['department'] == 'EMS','timeStamp']
#print(pd.to_datetime(ems_timestamp).dt.day_name().value_counts())
# print(pd.to_datetime(ems_timestamp).dt.weekday_name.value_counts())
# print(pd.to_datetime(ems_timestamp).dt.strftime('%A').value_counts())

'''
Compute --Create a countplot of the Day of Week column with the 
hue based of the Reason column & Question 6: On which day 
traffic calls were lowest?
'''
#table3['Day of Week'] = pd.to_datetime(table['timeStamp']).dt.weekday_name

#table3['Day of Week'] = pd.to_datetime(table['timeStamp']).dt.strftime('%A')

table3['Day of Week'] = pd.to_datetime(table['timeStamp']).dt.day_name()
sns.countplot(x="Day of Week",hue="department",data=table3[table3['department'] == "Traffic"]).set_title("Day of Week for Traffic")

'''
Compute --Create a countplot month wise 
--Question 7: Which month saw highest calls for fire?
'''
#table3['Month of Year'] = pd.to_datetime(table['timeStamp']).dt.strftime('%B')

table3['Month of Year'] = pd.to_datetime(table['timeStamp']).dt.month_name()
#sns.countplot(x="Month of Year",hue="department",data=table3[table3['department'] == "Fire"]).set_title("Month for Fire")

'''
Compute --Create Web Map for Traffic Calls & 
Question 8: Why some areas seem to have lower or almost zero 
traffic calls? Hint: Zoom the map
'''
#print(table3.shape)
#print(table3.dtypes)
# table3 = table.dropna()
# print("-------------")
# print(table3.isnull().values.any())
# print("-----")
# print(table3.isnull().sum())
# print("---------")
# print(table3.isnull().sum().sum())
# print("-------------")
# lon = table3.loc[table3['department']=="Traffic","lng"]
# lat = table3.loc[table3['department']=="Traffic","lat"]

# #print(lon)
# map=folium.Map(location=[lat.mean(),lon.mean()],zoom_start=6,tiles="MapBox Bright")
# map=folium.Map(location=[32.58,-99.09],zoom_start=6,tiles="MapBox Bright")
# fg=folium.FeatureGroup(name="Traffic Calls")

# for lt,ln in zip(lat,lon):
#       fg.add_child(folium.Marker(location=(lt,ln),popup="Traffic Call",icon=folium.Icon(color="blue")))

# map.add_child(fg)
# map.save("folium_1.html")
