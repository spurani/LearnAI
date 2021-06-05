# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:52:33 2021

@author: SP
"""
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import csv
'''
1.Write a program to enter a string from user and perform following tasks
•Write a python function named “Tokenize” which returns the tokenized string
•Print tokens along with the frequency of each tokenusing the above function
•Printthe 5 least occurring tokens
'''
fdist = FreqDist()

ui1 = """Gold is a chemical element with symbol Au (from Latin: aurum) and atomic number 79, making it one of the higher atomic number elements that occur naturally. In its purest form, it is a bright, slightly reddish yellow, dense, soft, malleable, and ductile metal. Chemically, gold is a transition metal and a group 11 element. It is one of the least reactive chemical elements and is solid under standard conditions. Gold often occurs in free elemental (native) form, as nuggets or grains, in rocks, in veins, and in alluvial deposits. It occurs in a solid solution series with the native element silver (as electrum) and also naturally alloyed with copper and palladium. Less commonly, it occurs in minerals as gold compounds, often with tellurium (gold tellurides).

Gold is resistant to most acids, though it does dissolve in aqua regia, a mixture of nitric acid and hydrochloric acid, which forms a soluble tetrachloroaurate anion. Gold is insoluble in nitric acid, which dissolves silver and base metals, a property that has long been used to refine gold and to confirm the presence of gold in metallic objects, giving rise to the term acid test. Gold also dissolves in alkaline solutions of cyanide, which are used in mining and electroplating. Gold dissolves in mercury, forming amalgam alloys, but this is not a chemical reaction.

A relatively rare element,[5][6] gold is a precious metal that has been used for coinage, jewelry, and other arts throughout recorded history. In the past, a gold standard was often implemented as a monetary policy, but gold coins ceased to be minted as a circulating currency in the 1930s, and the world gold standard was abandoned for a fiat currency system after 1971.

A total of 186,700 tonnes of gold exists above ground, as of 2015.[7] The world consumption of new gold produced is about 50% in jewelry, 40% in investments, and 10% in industry.[8] Gold's high malleability, ductility, resistance to corrosion and most other chemical reactions, and conductivity of electricity have led to its continued use in corrosion resistant electrical connectors in all types of computerized devices (its chief industrial use). Gold is also used in infrared shielding, colored-glass production, gold leafing, and tooth restoration. Certain gold salts are still used as anti-inflammatories in medicine. As of 2016, the world's largest gold producer by far was China with 450 tonnes per year"""

ui1_tokenize = word_tokenize(ui1)
#print(ui1_tokenize)
for word in ui1_tokenize:
    fdist[word.lower()] += 1
#print(fdist.most_common()[-5:])

'''
2.Write a program to enter a string from user and perform following tasks.
•Write a python function named “RemoveStopWords” which returns the string 
after removing stop words
•Count frequency of each stop word present in a string using the above function
•Plot a bar graph depicting stop wordsand their frequencies
'''

##Style 1 for removing stop words this is the most basic and simple method
en_stop_words = stopwords.words('English')
#print(en_stop_words)
re_stop = []
fdist1 = FreqDist()
for r in ui1_tokenize:
    if not r in en_stop_words:
        re_stop.append(r)
    if r in en_stop_words:
        fdist1[r.lower()] += 1
#print(re_stop)
#print(fdist1.items())
#fdist1.plot()

'''
3.Write a program to enter a string from user and perform following tasks
•Write a python functionnamed “Lemmatize” which returns a string after lemmatizing the string.
•Write a python functionnamed “Stemmed” which returns a string after stemming the string. 
(Use any stemmer of your preference)
•Print all the words along with their lemmatized and stemmed form using theabove functions
•Save these results in a csv file having 3 columns:
'''
string_to_lematize = "program programmer programming programs programmers"
ui2_tokenize = word_tokenize(string_to_lematize)
word_lem = WordNetLemmatizer()
pst = PorterStemmer()
f = open("casestudy.csv", "w",newline='')
writer = csv.DictWriter(
    f, fieldnames=["Original", "Lemmatized Form", "Stemmed Form"])
writer.writeheader()
for a in ui2_tokenize:
    writer.writerow({"Original" : a,"Lemmatized Form" : word_lem.lemmatize(a,wordnet.NOUN), "Stemmed Form" : pst.stem(a)})
f.close()
