# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:52:32 2020

@author: SP
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

books = pd.read_csv('BX-Books.csv',encoding="ISO-8859-1").head(10000)
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher']
users = pd.read_csv('BX-Users.csv',encoding="ISO-8859-1").head(10000)
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('BX-Book-Ratings.csv',encoding="ISO-8859-1").head(1000)
ratings.columns = ['userID', 'ISBN', 'bookRating']
data_books_ratings = pd.merge(books,ratings,on="ISBN")
data_users_ratings = pd.merge(users,ratings,on="userID")
print(data_books_ratings.columns)
print(data_users_ratings.columns)
data = pd.merge(data_users_ratings,data_books_ratings,on=["userID"])
print(data)
n_users = ratings.userID.unique().shape[0]
n_books = ratings.ISBN.unique().shape[0]
train_data, test_data = train_test_split(ratings, test_size = 0.25)
train_data_matrix = np.zeros((n_users, n_books))
for line in train_data.itertuples():
    train_data_matrix[line[1]-1,line[2]-1] = line[3]
print(train_data_matrix)

# books = pd.read_csv('BX-Books.csv', encoding="ISO-8859-1")
# books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher']
# users = pd.read_csv('BX-Users.csv', encoding="ISO-8859-1")
# users.columns = ['userID', 'Location', 'Age']
# ratings = pd.read_csv('BX-Book-Ratings.csv', encoding="ISO-8859-1")
# ratings.columns = ['userID', 'ISBN', 'bookRating']
# rating_count = pd.DataFrame(ratings.groupby('ISBN')['bookRating'].count())
# rating_count = rating_count.sort_values('bookRating', ascending=False).head()
# most_rated_books = pd.DataFrame(['0971880107', '0316666343', '0385504209', '0060928336', '0312195516'], index=np.arange(5), columns = ['ISBN'])
# most_rated_books_summary = pd.merge(most_rated_books,books,on='ISBN')
# print(most_rated_books_summary)