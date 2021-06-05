# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:38:56 2021

@author: SP
"""

import nltk
import os
import string
import nltk.corpus
from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
#print(os.listdir(nltk.data.find("corpora")))
print(twitter_samples.fileids())
print(nltk.corpus.gutenberg.fileids())
macbeth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
#outputfile = open("macbeth.txt",'w')
#for word in macbeth:
#    print(word,sep=' ',end=' ',file= outputfile)
#outputfile.close()
#outputfile = open("macbeth-ArticlesRemoved.txt",'w')

print("a: ",macbeth.count("a"))
print("an: ",macbeth.count("an"))
print("the: ",macbeth.count("the"))

#stopwords = ['a', 'an','the']
#outputfilearticles = open('macbeth-ArticlesRemoved.txt','w') 

#for r in macbeth:
#    if not r in stopwords:
#        print(r,sep=' ',end=' ',file= outputfilearticles)
#outputfilearticles.close()

#outputfilepunctuations = open('macbeth-PunctuationsRemoved.txt','w') 

#for wording in macbeth:
#    w = wording.translate(str.maketrans('', '', string.punctuation))
#    print(w,sep=' ',end=' ',file=outputfilepunctuations)
#outputfilepunctuations.close()

femalenames = nltk.corpus.names.words('female.txt')
print("Female names: ",len(femalenames))
malenames = nltk.corpus.names.words('male.txt')
print("Male names: ",len(malenames))


cfd = nltk.ConditionalFreqDist((fileid, name[-1])
                            for fileid in nltk.corpus.names.fileids()
                            for name in nltk.corpus.names.words(fileid))
fig = plt.figure(figsize = (10,4))
cfd.plot()
fig.show()
fig.savefig('FrequencyOfNamesOfEachAlphabet.png')