# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 07:58:20 2021

@author: SP
"""
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

def MakeCorpus(s1,s2,s3):
    s1_tokenize = word_tokenize(s1)
    s2_tokenize = word_tokenize(s2)
    s3_tokenize = word_tokenize(s3)
    corpus = list(dict.fromkeys(s1_tokenize + s2_tokenize + s3_tokenize))
    print(corpus)
MakeCorpus("India won the match","England won the cricket match","Australia won the final match")

def PresenceAbsenceVectorization(s1,s2,s3):
    pav = [s1,s2,s3]
    count_vec = CountVectorizer()
    X_counts = count_vec.fit_transform(pav)
    X_names = count_vec.get_feature_names()
    a = pd.DataFrame(X_counts.toarray(),columns = X_names)
    print(a)
PresenceAbsenceVectorization("India won the match","England won the cricket match","Australia won the final match")


def CountVectorization(s1,s2,s3):
    s1_tokenize = word_tokenize(s1)
    s2_tokenize = word_tokenize(s2)
    s3_tokenize = word_tokenize(s3)
    pav = [s1,s2,s3]
    print(pav)
    #corpus = list(dict.fromkeys(pav))
    #print(corpus)
    count_vec = CountVectorizer()
    X_counts = count_vec.fit_transform(pav)
    X_names = count_vec.get_feature_names()
    print(X_names)
    a = pd.DataFrame(X_counts.toarray(),columns = X_names)
    print(a)
CountVectorization("A lives with B. A plays with C","B lives with C. B plays with D","C lives with D. C plays with A")

def TfidfVectorizertest(s1,s2,s3):
    tfvectlist = [s1,s2,s3]
    tf_vect = TfidfVectorizer()
    tf_matrix = tf_vect.fit_transform(tfvectlist)
    tf_names = tf_vect.get_feature_names()
    print(tf_names)

TfidfVectorizertest("India won the match","England won the cricket match","Australia won the final match")