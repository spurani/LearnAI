# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 05:21:30 2020

@author: SP
"""
import pandas as pd
import numpy as np

'''
1.Create a pandas dataframe having following structure
float_col  int_col str_col0       0.1      1a1        0.22b2        0.26None3       10.18c4        NaN      -1       a
'''

table = pd.DataFrame({'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']})
#print(table)

'''
2.filter  the  columns  'float_col',  'int_col'  from  the  
dataframe  in  one  query.  Hint-use  ix method of dataframes. 
Also print without using ix method
'''
table1 = table
table1 = table1.filter(items=['float_col','int_col'])
#print(table1)

table2 = table
#print(table2.loc[:,['float_col','int_col']])

'''
3.filter the records from float_col having value greater than 0.15 
and in separate query filter float_col value equal to 0.1
'''
table3 = table
#print(table3.loc[table3['float_col'] > 0.15])

table4 = table
#print(table4.loc[table4['float_col'] > 0.1])

'''
4.filter  the  records  from data  framewhich  satisfies  
both  the  conditions  float_col greater than 0.1 and int_col 
greater than 2
'''
table5 = table
#print(table5.loc[(table5['float_col'] > 0.1) & (table5['int_col'] > 2)])

'''
5.filter  the  records  from  data  frame  which  satisfies  
both  the  conditions  float_col greater than 0.1 or int_col
greater than 2
'''
table6 = table
#print(table6.loc[(table6['float_col'] > 0.1) | (table6['int_col'] > 2)])

'''
6.filter the records from data frame which satisfies the 
conditions float_col not greater than 0.1
'''
table7 = table
#print(table7.loc[(table7['float_col'] < 0.1)])

'''
7.Create a new data frame in which column int_col is renamed to 
new_name.
8.Modify the existing dataframe and rename the column int_col to 
new_name
'''
table8 = table
#print(table8.rename(index=str,columns={'int_col':'new_name'}))
#print(table8.rename(index=str,columns={'int_col':'new_name'}))

'''
9.Drop the rows where any value is missing from the dataframe
'''
table9 = table
#print(table9.dropna())

'''
10.Change the missing value in column float_col as mean value of the float_col
'''
q_10 = table
#print(q_10['float_col'].fillna(q_10['float_col'].mean()))

'''
11.change  all  the  values  of  str_col  with  new  value and  
drop  the  missing  values.  New value should have prefixmap_ 
and original value. Eg map_a, map_b
'''
q_11 = table
q_11 = q_11['str_col'].map('map_{}'.format)
#print(q_11.drop(2))
'''
12.group  all  the  values  of  str_col  and  find  the  mean  of  
float_col  in  all  the  groups respectively.
'''
grouped = table['float_col'].groupby(table['str_col'])
#print(grouped.mean())

'''
13.find the covariance of float_col and int_col
'''
#q_13 = table
#print(np.corrcoef(q_13['float_col'],q_13['int_col']))

'''
14.find the correlation of float_col and int_col
'''
q_14 = table.filter(items=['float_col','int_col'])
#print(q_14.corr())

'''
15.Create a data frame ‘other’ having columns some_val and str_col having values given belowsome_val str_col0         1       a1         2       bPerform inner join, outer join, left join and right join with data frame x
'''

other = pd.DataFrame({'some_val':[1,2],'str_col':['a','b']})
l = pd.merge(other,table,on='str_col')
print(l)

l = pd.merge(other,table,on='str_col',how='inner')
print(l)

l = pd.merge(other,table,on='str_col',how='outer')
print(l)

l = pd.merge(other,table,on='str_col',how='left')
print(l)

l = pd.merge(other,table,on='str_col',how='right')
print(l)

'''
16.When we want to send the same invitations to many people,
the body of the mail does not change. Only the name (and maybe 
address) needs to be changed.Mail  merge  is  a  process  of  
doing  this.  Instead  of  writing  each  mail  separately, we              have  a  template  for  body  of  the  mailand  a  list  of  names  that  we  merge together to form all the mails.Create a text file “names.txt” having the names.Anilsunita
'''

# file_object = open("names.txt","r")
# file_object_1 = open("content.txt","r")
# body = file_object_1.read()
# for i in file_object:
#         i = i.strip("\n")
#         file_object_2 = open(i+".txt","w+")
#         mail = "Hello " + i +"\n"+body
#         file_object_2.write(mail)

# ---------------------------------------------
print(other.join(table.set_index('str_col'), on ='str_col'))
print(other.set_index('str_col').join(table.set_index('str_col')))

