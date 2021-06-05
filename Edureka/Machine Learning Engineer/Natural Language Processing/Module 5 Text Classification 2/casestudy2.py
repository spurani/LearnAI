# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 22:07:51 2021

@author: SP
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
stop_words=stopwords.words('english')
labelencoder = LabelEncoder()
data = pd.read_csv("698_m5_datasets_v1.0/Eopinions.csv")
data['Label'] = labelencoder.fit_transform(data['class'])
#data['class'].value_counts().plot.bar()
data['text'] = data['text'].str.replace("[-.?!_,:;()|0-9]","")
data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
data['text'] = data['text'].str.lower()
data['Preprocessed'] = data['text'].apply(word_tokenize)
countvector = CountVectorizer()
X_counts = countvector.fit_transform(data['text']).toarray()
d = pd.DataFrame(columns=['CountVector'])
for i in X_counts:
    d = d.append({'CountVector' : i},ignore_index=True)
data = pd.concat([d,data],axis=1)
data.to_csv("Eopinions.csv")

#X_counts_df = pd.DataFrame(X_counts.toarray(),columns=countvector.get_feature_names())

label = []
for i in data['Label']:
    label.append(i)
label = pd.Series(label)
#print(X_counts_df)
# print(label)
print(data['Label'])
#X_train, X_test, y_train, y_test = train_test_split(data['text'],data['Label'], test_size=0.20, random_state=42, shuffle=True)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
# #countvector = CountVectorizer()
#df_train = pd.DataFrame(countvector.fit_transform(X_train).todense(),columns=countvector.get_feature_names())
#df_test = pd.DataFrame(countvector.transform(X_test).todense(),columns=countvector.get_feature_names())
#print(df_train)
# print(df_train.shape)
# print(df_test.shape)
# print(y_train.shape)
# print(y_test.shape)
# print(df_train)
# print(df_test)
# gnb = GaussianNB()
# y_predict = gnb.fit(df_train, y_train).predict(df_test)
# print(y_predict)
# lr = LogisticRegression()
# y_predict_lr = lr.fit(df_train,y_train).predict(df_test)
# print(y_predict_lr)