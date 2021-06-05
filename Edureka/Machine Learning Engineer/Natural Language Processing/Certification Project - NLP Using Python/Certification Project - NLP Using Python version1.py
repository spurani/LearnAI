# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:55:53 2021

@author: SP
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 03:42:37 2021

@author: SP
"""

import os
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.stem.porter import PorterStemmer
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from collections import Counter
from scipy.sparse.csr import csr_matrix 
rootdir = 'BBC News Articles'
data_list = []
data = pd.DataFrame()
i = 1
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file = open(os.path.join(subdir, file), encoding='utf-8')
        line = file.read().replace("\n","")
        ##convert each line to lowercase
        data.set_value(i,'ArticleType',subdir.rsplit("\\")[-1])
        data.set_value(i,'Article',line.lower())
        file.close()
        i+=1
#data.to_csv("BBCNewsArticles.csv",index=False)
#data['Articlenopunctuations'] = data['Article'].str.replace("[.,]","")
#data['Articlenopunctuations'] = data['Article'].str.replace("['']"," ")

##Remove punctuations,numbers
data['Articlenopunctuations'] = data['Article'].str.replace("[^a-zA-Z\s]"," ")
stop = stopwords.words('english')
ps = PorterStemmer()

##Remove stopwords
data['Articlenostopwords']= data['Articlenopunctuations'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

## Stemming
data['Articlepreprocessed'] = data['Articlenostopwords'].apply(lambda x: ' '.join([ps.stem(word) for word in x.split()]))

##Convert preprocessed(no punctuations, no stop words, stemmed, lowercase, no blanklines) articles to tokens
data['Articletokens'] = data['Articlepreprocessed'].apply(word_tokenize)
data['ArticleType_id'] = data['ArticleType'].factorize()[0]
data.to_csv("BBCNewsArticles.csv",index=False)

###Analysis

##Code below spits out most frequent words with its count present in each document category
for group_name, subset in data.groupby('ArticleType'):
    sentimentData=subset['Articlepreprocessed']
    words=[]
    for each in sentimentData:
        words.extend(each.split(" "))
    print(group_name)
    print(Counter(words).most_common(15))
    print()
##
###

##Prepare labels##
articletype = data[['ArticleType','ArticleType_id']].drop_duplicates().sort_values('ArticleType_id')
category_to_id = dict(articletype.values)
id_to_category = dict(articletype[['ArticleType_id','ArticleType']].values)
# print(id_to_category)
# print(articletype)
# print(category_to_id)
#exit
##
all_words = []
for i in data['Articletokens']:
    for j in i:
        all_words.append(j)
corpus_tokens = list(set(all_words))
print(corpus_tokens)

detokenizelist = []
detokenizer = TreebankWordDetokenizer()
for k in data['Articletokens']:
        detokenizelist.append(detokenizer.detokenize(k))
print(detokenizelist)

number_of_clusters=5

'''PresenceAbsence Vector'''
articlepavector = []
datat=[]
indices = []
for j in data['Article']:
    vector = []
    for k in j:
        if(k in corpus_tokens):
            vector.append(1)
        else:
            vector.append(0)
    articlepavector.append(vector)

pca = PCA(n_components=2).fit(articlepavector)
data2Dpav = pca.transform(articlepavector)

km = KMeans(n_clusters=number_of_clusters)
km.fit(articlepavector)
# #pd.crosstab(km.labels_, data["Articlepreprocessed"])
# label = kmcountvector.predict(X_counts)
print(f'Silhouette Score(n=5): {silhouette_score(articlepavector, km.labels_)}')

'''Count Vector'''
# countvector = CountVectorizer()
# X_counts = countvector.fit_transform(corpus_tokens).todense()
# X_names = countvector.get_feature_names()

# pcacv = PCA(n_components=2).fit(X_counts)
# data2Dcv = pcacv.transform(X_counts) 

# kmcountvector = KMeans(n_clusters=number_of_clusters)
# kmcountvector.fit(data2Dcv)
# labelcsv = pd.DataFrame(kmcountvector.labels_).to_csv("BBCNewsArticlesClustered.csv")

# plt.figure(1)
# plt.scatter(data2Dcv[:, 0], data2Dcv[:, 1], c=kmcountvector.labels_, s=50, cmap='viridis')
# centers = kmcountvector.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='white', s=200, alpha=0.5)
# for i, c in enumerate(centers):
#         plt.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
#                     s=50, edgecolor='k')
# print('Silhouette Score(n=5): %0.3f'% silhouette_score(data2Dcv, kmcountvector.labels_))

'''TFID VECTOR'''
# tf_vect = TfidfVectorizer()
# tf_matrix = tf_vect.fit_transform(detokenizelist).todense()
# tf_names = tf_vect.get_feature_names()

# pca = PCA(n_components=2).fit(tf_matrix)
# data2D = pca.transform(tf_matrix)  

# kmtfvect = KMeans(n_clusters=number_of_clusters)
# kmtfvect.fit(data2D)
# labelcsv = pd.DataFrame(kmtfvect.labels_).to_csv("BBCNewsArticlesClustered.csv",mode='a')
# plt.figure(2)
# plt.scatter(data2D[:, 0], data2D[:, 1], c=kmtfvect.labels_, s=50, cmap='viridis')
# centers = kmtfvect.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c='white', s=200, alpha=0.5)
# for i, c in enumerate(centers):
#         plt.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
#                     s=50, edgecolor='k')
# print('Silhouette Score(n=5): %0.3f'% silhouette_score(data2D, kmtfvect.labels_))

'''
Provide your explanation for the following questions 
1.What does Silhouette Coefficient tell us?
Ans: Silhouette Coefficient's are calculated based on mean intra-cluster 
distance and nearest cluster distance distance between each sample. It is measured
between -1 to +1 closer the values to +1 means samples are assigned to accurate/appropriate
clusters. 

2.Which algorithm you chose and why?
Ans: I chose Kmeans algorithm as that is simpliest unsupervised clustering algorithm.
which forms clusters based passed n_clusters.one of the fastest clustering algorithms available

3.Can you provide an appropriate name to a cluster label? 
If yes, then explain your observations.
Yes According to the figure here is the cluster mapping (0 -> business),(1 -> entertainment)
(2->politics), (3->sports) (4->tech)
4.Which vectorization technique is the best and why?
Ans: TF-IDF no doubt as it tokenizes words on its own after passsing list of string to it.
Term Frequency - Inverse Document Frequency is widely used in clustering for classification of documents.
removes all duplicates and scales down the tokens which are less informative and occur more frequently
'''
