# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 18:22:11 2021

@author: SP
"""

import pandas as pd
from nltk import RegexpParser, word_tokenize, pos_tag

data = pd.read_csv("698_m3_datasets_v1.0/tweets.csv")
text = data.loc[data['text'].str.startswith('@'),'text']
references = open("References.txt","w+", errors="ignore")
for i in text:
    if(i.startswith('@') == True):
        #print(i)
        references.write(i+"\n")
references.close()

text_airline_sentiment = data.loc[(data['airline_sentiment'] == 'negative'),['airline_sentiment','text']]
#print(text_airline_sentiment)
grammer_noun = r"NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammer_noun)
references_negative_airline_sentiment = open("References_negative_airline_sentiment.txt","w+", errors="ignore")
for i in text_airline_sentiment.values:
    if(i[1].startswith('@') == True):
        print(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
        #print(i[0]+" => "+i[1])
        references_negative_airline_sentiment.write(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
references_negative_airline_sentiment.close()

text_airline_sentiment = data.loc[(data['airline_sentiment'] == 'neutral'),['airline_sentiment','text']]
#print(text_airline_sentiment)
grammer_noun = r"NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammer_noun)
references_negative_airline_sentiment = open("References_neutral_airline_sentiment.txt","w+", errors="ignore")
for i in text_airline_sentiment.values:
    if(i[1].startswith('@') == True):
        #print(i[0]+" => "+i[1])
        references_negative_airline_sentiment.write(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
references_negative_airline_sentiment.close()

text_airline_sentiment = data.loc[(data['airline_sentiment'] == 'positive'),['airline_sentiment','text']]
#print(text_airline_sentiment)
grammer_noun = r"NP: {<DT>?<JJ>*<NN>}"
chunk_parser = RegexpParser(grammer_noun)
references_negative_airline_sentiment = open("References_positive_airline_sentiment.txt","w+", errors="ignore")
for i in text_airline_sentiment.values:
    if(i[1].startswith('@') == True):
        #print(i[0]+" => "+i[1])
        references_negative_airline_sentiment.write(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
references_negative_airline_sentiment.close()





text_airline_sentiment = data.loc[(data['airline_sentiment'] == 'negative'),['airline_sentiment','text']]
#print(text_airline_sentiment)
grammer_noun = r"VP: {<VB>}"
chunk_parser = RegexpParser(grammer_noun)
references_negative_airline_sentiment = open("References_vb_negative_airline_sentiment.txt","w+", errors="ignore")
for i in text_airline_sentiment.values:
    if(i[1].startswith('@') == True):
        print(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
        #print(i[0]+" => "+i[1])
        references_negative_airline_sentiment.write(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
references_negative_airline_sentiment.close()

text_airline_sentiment = data.loc[(data['airline_sentiment'] == 'neutral'),['airline_sentiment','text']]
#print(text_airline_sentiment)
grammer_noun = r"VP: {<VB>}"
chunk_parser = RegexpParser(grammer_noun)
references_negative_airline_sentiment = open("References_vb_neutral_airline_sentiment.txt","w+", errors="ignore")
for i in text_airline_sentiment.values:
    if(i[1].startswith('@') == True):
        #print(i[0]+" => "+i[1])
        references_negative_airline_sentiment.write(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
references_negative_airline_sentiment.close()

text_airline_sentiment = data.loc[(data['airline_sentiment'] == 'positive'),['airline_sentiment','text']]
#print(text_airline_sentiment)
grammer_noun = r"VP: {<VB>}"
chunk_parser = RegexpParser(grammer_noun)
references_negative_airline_sentiment = open("References_vb_positive_airline_sentiment.txt","w+", errors="ignore")
for i in text_airline_sentiment.values:
    if(i[1].startswith('@') == True):
        #print(i[0]+" => "+i[1])
        references_negative_airline_sentiment.write(chunk_parser.parse(pos_tag(word_tokenize(i[1]))))
references_negative_airline_sentiment.close()