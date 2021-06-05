# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 18:38:07 2021

@author: SP
"""
import pandas as pd
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem import WordNetLemmatizer
detokenizer = TreebankWordDetokenizer().detokenize
lemmatizer = WordNetLemmatizer()
count_vect = CountVectorizer()
stop = stopwords.words('english')
def lemmatize_text(text):
    return [lemmatizer.lemmatize(w) for w in word_tokenize(text)]
data = pd.read_csv("winemag-data_first150k.csv",encoding="utf8")
description = data['description'].str.replace(r'[-.?!,:;()%|0-9]','')
description = description.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
data['Refined-Description'] = description.apply(word_tokenize)
#print(data['Refined-Description'])
data['Refined-Description'] = description.apply(lemmatize_text)
#print(data['Refined-Description'])
data['detokenized_refined_string'] = data['Refined-Description'].apply(detokenizer)

corpus = []
for i in data['Refined-Description']:
    for j in i:
        corpus.append(j)
#print(corpus)

corpus_string = []
for i in data['detokenized_refined_string']:
    corpus_string.append(i)
#print(corpus_string)

count_vect = CountVectorizer(lowercase=True)
X_counts = count_vect.fit_transform(corpus_string)
print(X_counts.toarray())
lst = []
for i in X_counts.toarray():
    lst.append(i)
data['CountVectorization'] = lst
tfidvect = TfidfVectorizer(lowercase=True)
tfidmatrix = tfidvect.fit_transform(corpus_string)
print(tfidmatrix.todense())
lst2 = []
for i in tfidmatrix.todense():
    lst2.append(i)
data['TF-IDVECTORIZATION'] = lst2
data.to_csv("new.csv")