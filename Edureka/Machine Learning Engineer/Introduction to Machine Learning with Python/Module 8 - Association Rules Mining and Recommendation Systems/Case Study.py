# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:52:32 2020

@author: SP
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import pairwise_distances

books = pd.read_csv('BX-Books.csv',encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher']
users = pd.read_csv('BX-Users.csv',encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('BX-Book-Ratings.csv',encoding="latin-1",nrows=10000)
ratings.columns = ['userID', 'ISBN', 'bookRating']
data_books_ratings = pd.merge(ratings,books,on="ISBN")
print(data_books_ratings['bookRating'].head())

n_users = data_books_ratings.userID.nunique()
n_books = data_books_ratings.ISBN.nunique()
print(n_users)
print(n_books)
isbn_list = data_books_ratings['ISBN'].unique()
userid_list = data_books_ratings['userID'].unique()
def get_isbn_numeric_id(isbn):
    #print ("  isbn is:" , isbn)
    itemindex = np.where(isbn_list==isbn)
    return itemindex[0][0]

def get_user_id_numeric_id(user_id):
    #print ("  isbn is:" , isbn)
    itemindex = np.where(userid_list==user_id)
    return itemindex[0][0]

data_books_ratings['user_id_order'] = data_books_ratings['userID'].apply(get_user_id_numeric_id)
data_books_ratings['isbn_id'] = data_books_ratings['ISBN'].apply(get_isbn_numeric_id)

new_col_order = ['user_id_order', 'isbn_id', 'bookRating', 'bookTitle', 'bookAuthor','yearOfPublication','publisher','ISBN','userID']
data_books_ratings = data_books_ratings.reindex(columns= new_col_order)
print(data_books_ratings.head())
train_data, test_data = train_test_split(data_books_ratings, test_size = 0.30)
train_data_matrix = np.zeros((n_users, n_books))
for line in train_data.itertuples():
    train_data_matrix[line[1]-1,line[2]-1] = line[3]
print(train_data_matrix)

test_data_matrix = np.zeros((n_users, n_books))
for line in test_data.itertuples():
    test_data_matrix[line[1]-1, line[2]-1] = line[3]
print(test_data_matrix)

user_similarity = pairwise_distances(train_data_matrix, metric='cosine')
item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')
def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        #You use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis]) 
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])     
    return pred
item_prediction = predict(train_data_matrix, item_similarity, type='item')
user_prediction = predict(train_data_matrix, user_similarity, type='user')
from sklearn.metrics import mean_squared_error
from math import sqrt
def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten() 
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))
print('User-based CF RMSE: ' + str(rmse(user_prediction, test_data_matrix)))
print('Item-based CF RMSE: ' + str(rmse(item_prediction, test_data_matrix)))