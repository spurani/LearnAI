# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:33:30 2020

@author: SP
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
table = pd.read_csv("775_m7_datasets_v1.0/HollywoodMovies.csv")

#From the data provided on Hollywood movies:

'''
1.Find the highest rated movie in the “Quest” story type.
'''
#q_one_first = table.loc[(table['Story'] == "Quest")]
#q_one_two = table.loc[((table["RottenTomatoes"] == table["RottenTomatoes"].max()) | (table["AudienceScore"] == table["AudienceScore"].max()))]
#print(q_one_two[['Movie','RottenTomatoes','AudienceScore']])

'''
2.Find the genre in which there has been the greatest number of movie releases
'''
#print(table.groupby('Genre')['Movie'].count())

'''
3.Print the names of the top five movies with the costliest budgets.
'''
#print(table.groupby('Movie')['Budget'].max().nlargest())

'''
4.Is there any correspondence between the critics’ evaluation of a movie and itsacceptance 
by the public? Find out, by plotting the net profitability of a movie against the ratings it 
receives on Rotten Tomatoes.
'''
#selected_data = table.loc[:,['Movie','RottenTomatoes','AudienceScore','Profitability']]
#x = np.array(selected_data['RottenTomatoes'])
#y = np.array(selected_data['Profitability'])
#plt.scatter(x,y)

'''
5.Perform Operations on Files
'''

'''
5.1: From the raw data below create a data frame
'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
'age': [42, 52, 36, 24, 73], 
'preTestScore': [4, 24, 31, ".", "."],
'postTestScore': ["25,000", "94,000", 57, 62, 70]
'''
# first_name = ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
# last_name = ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
# age = [42, 52, 36, 24, 73], 
# preTestScore = [4, 24, 31, ".", "."],
# postTestScore = ["25,000", "94,000", 57, 62, 70]
# data = {'First Name':['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],'Last Name':['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],'Age':[42, 52, 36, 24, 73],'Pre Test Score':[4, 24, 31, ".", "."],'Post Test Score':["25,000", "94,000", 57, 62, 70]}
# df = pd.DataFrame(data)
# print(df)

'''
5.2: Save the dataframe into a csv file as example.csv
'''
# df.to_csv("example.csv")

'''
5.3: Read the example.csv and print the data frame
'''
# df1 = pd.read_csv("example.csv")
# print(df1)

'''
5.4: Read the example.csv without column heading
'''
#df2 = pd.read_csv("example.csv",header=None,skiprows=1)
#print(df2)

'''
Question 5: Read the example.csv and make the index columns as 'First Name’ and
'Last Name'
'''
#df3 = pd.read_csv("example.csv")
#df3.rename( columns={'Unnamed: 0':'First Name and Last Name'}, inplace=True )
#print(df3)

'''
5.6: Print the dataframe in a Boolean form as True or False. True for Null / NaN 
values and false for non-nullvalues
'''
#print(df3.isnull())

'''
5.7: Read the dataframe by skipping first 3 rows and print the data frame
'''
#print(df3.tail(2))

'''
5.8: Load a csv file while interpreting "," in strings around numbers as 
thousands seperators. Check the raw data 'postTestScore' column has, as 
thousands separator. 
'''
#df4 = pd.read_csv("example.csv",thousands=',')
#print(df4)

'''
6.Perform Operations on Files
'''

'''
6.1: From the raw data below create a Pandas Series
'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'
a) Print all elements in lower case
b) Print all the elements in upper case
c) Print the length of all the elements
'''

#q_six_one = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
#print(q_six_one.str.lower())
#print(q_six_one.str.upper())
#print(q_six_one.str.len())

'''
6.2: From the raw data below create a Pandas Series
' Atul', 'John ', ' jack ', 'Sam'
a) Print all elements after stripping spaces from the left and right
b) Print all the elements after removing spaces from the left only
c) Print all the elements after removing spaces from the right only
'''

#q_six_two = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
#print(q_six_two.str.replace(" ",""))
#print(q_six_two.str.lstrip())
#print(q_six_two.str.rstrip())

'''
6.3: Create a series from the raw data below
'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'
a)split the individual strings wherever ‘_’ comes and create a list out of it.
b)Access the individual element of a list
c)Expand the elements so that all individual elements get splitted by ‘_’ 
and insted of list returns individual elements
'''
# q_six_three = pd.Series(['India_is_big', 'Population_is_huge','Has_diverse_culture'])
# q_c = []
# for i in range(len(q_six_three)):
#           q_c.append(q_six_three[i].split("_"))

# for i in range(len(q_c)):
#     print(q_c[i])

'''
6.4: Create a series and replace either X or dog with XX-XX
'A', 'B', 'C', 'AabX','BacX','', np.nan, 'CABA', 'dog', 'cat'
'''
#q_six_point_four = pd.Series(['A', 'B', 'C', 'AabX','BacX','', np.nan, 'CABA', 'dog', 'cat'])
#print(q_six_point_four)

# q_six_point_four = q_six_point_four.str.replace('X','XX-XX')
# print(q_six_point_four)

# q_six_point_four = q_six_point_four.replace('dog','XX-XX')
# print(q_six_point_four)

'''
6.5: Create a series and remove dollar from the numeric values
'12', '-$10', '$10,000'
'''
# q_six_point_five = pd.Series(['12', '-$10', '$10,000'])
# print(q_six_point_five)

# q_six_point_five = q_six_point_five.str.replace("$","")
# print(q_six_point_five)

'''
6.6:-Create a series and reverse all lower case words
'india 1998', 'big country', np.nan
'''
# pat=r'[a-z]+'
# repl=lambda m: m.group(0)[::-1]
# s=pd.Series(['india 1998', 'big country', np.nan]).str.replace(pat,repl)
# print (s)
'''
6.7: Create pandas series and print true if value is alphanumeric in series or
false if value is not alpha numeric in series.'1', '2', '1a', '2b', '2003c'
'''
#q_six_point_seven = pd.Series(['1', '2', '1a', '2b', '2003c'])
#print(q_six_point_seven.str.isalnum())

'''
6.8: Create pandas series and print true if value is containing 
‘A’'1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'
'''
#q_six_point_eight = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
#print(q_six_point_eight.str.contains('A'))

'''
6.9: Create pandas series and print in three columns value 0 or 1 is a or b or c 
exists in values'a', 'a|b', np.nan, 'a|c'
'''
s=pd.Series(['a', 'a|b', np.nan, 'a|c'])
print (s.str.get_dummies(sep='|'))
'''
6.10: Create pandas dataframe having keys and ltable and rtable as below -
'key': ['One', 'Two'], 'ltable': [1, 2]
'key': ['One', 'Two'], 'rtable': [4, 5]
Merge both the tables based of key
'''
# df1 = pd.DataFrame({'A':[1],'B':[2]})
# df2 = pd.DataFrame({'A':[4],'B':[5]})
# print(df1)
# print(df2)
# print(pd.merge(df1,df2))