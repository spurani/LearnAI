# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:47:33 2021

@author: SP
"""
import docx
from nltk import word_tokenize,ngrams,bigrams,trigrams,FreqDist,pos_tag,ne_chunk,Tree
from collections import Counter
from matplotlib import pyplot as plt
doc = docx.Document("698_m2_datasets_v1.0\Brexit.docx")
fullText = []
for para in doc.paragraphs:
    fullText.append(para.text)
fullText = '\n'.join(fullText)

def GetNGrams(string):
     fulltext_tokenize = word_tokenize(string.lower())
     print(list(bigrams(fulltext_tokenize)))
     print(list(trigrams(fulltext_tokenize)))
     print(list(ngrams(fulltext_tokenize,4)))
     bl = list(bigrams(fulltext_tokenize))
     freqdist = FreqDist(bl).most_common()
     print(freqdist)
     
def NounsCount(string):
     fulltext_tokenize = word_tokenize(string.lower())
     pos_fulltext = pos_tag(fulltext_tokenize)
     counter = [token for token, pos in pos_fulltext if pos.startswith('NN')]
     counter_m = [(token,pos) for token, pos in pos_fulltext if pos.startswith('NN')]
     #print(counter_m)
     #print(len(counter))
     freqdist = FreqDist(counter)
     freqdist.plot()
     fredist_f = FreqDist(counter_m).most_common()
     print(fredist_f)
     return len(counter)
    
def PronounsCount(string):
    fulltext_tokenize = word_tokenize(string.lower())
    pos_fulltext = pos_tag(fulltext_tokenize)
    counter = [token for token, pos in pos_fulltext if pos.startswith('PRP')]
    freqdist = FreqDist(counter)
    freqdist.plot()
    return len(counter)

def AdjectivesCount(string):
    fulltext_tokenize = word_tokenize(string.lower())
    pos_fulltext = pos_tag(fulltext_tokenize)
    counter = [token for token, pos in pos_fulltext if pos.startswith('JJ')]
    freqdist = FreqDist(counter)
    freqdist.plot()
    return len(counter)

    
def VerbsCount(string):
    fulltext_tokenize = word_tokenize(string.lower())
    pos_fulltext = pos_tag(fulltext_tokenize)
    counter = [token for token, pos in pos_fulltext if pos.startswith('VB')]
    freqdist = FreqDist(counter)
    freqdist.plot()
    return len(counter)
    
def AdverbsCount(string):
    fulltext_tokenize = word_tokenize(string.lower())
    pos_fulltext = pos_tag(fulltext_tokenize)
    counter = [token for token, pos in pos_fulltext if pos.startswith('RB')]
    freqdist = FreqDist(counter)
    freqdist.plot()
    return len(counter)
    
GetNGrams(fullText)

nc = NounsCount(fullText)
pc = PronounsCount(fullText)
ajc = AdjectivesCount(fullText)
adc = AdverbsCount(fullText)
vc =  VerbsCount(fullText)
labels = 'Nouns', 'Pronouns', 'Adjectives', 'Adverbs', 'Verbs'
sizes = [nc,pc,ajc,adc,vc]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


###This function returns the list of chunks/tokens of specific label ['chicago'] which is GPE
def get_continuous_chunks(text, label):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for subtree in chunked:
        if type(subtree) == Tree and subtree.label() == label:
            current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
        if current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk
########################################################################

###This function returns tupple with text and its label ('chicago','GPE')
def get_chunks_with_its_labels(text, label):
    tag_with_token= []
    tokenized_doc = word_tokenize(text)
    tagged_sentences = pos_tag(tokenized_doc)
    NE= ne_chunk(tagged_sentences )
    named_entities = []
    for tagged_tree in NE:
        #print(tagged_tree)
        if hasattr(tagged_tree, 'label'):
          entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) #
          entity_type = tagged_tree.label() # get NE category
          named_entities.append((entity_name, entity_type))
    #print(named_entities)  #all entities will be printed,check at your end once
    for tag in named_entities:
      #print(tag)
      #print(tag[1])
      if tag[1]==label:   #Specify any tag which is required
        tag_with_token.append(tag)
    return tag_with_token
################################################

def GeoPoliticalCount(string):
    print(get_continuous_chunks(string,'GPE'))
    print(len(get_continuous_chunks(string,'GPE')))

def PersonsCount(string):
    print(get_continuous_chunks(string,'PERSON'))
    print(len(get_continuous_chunks(string,'PERSON')))

def OrganizationCount(string):
    print(get_continuous_chunks(string,'ORGANIZATION'))
    print(len(get_continuous_chunks(string,'ORGANIZATION')))

GeoPoliticalCount(fullText)
PersonsCount(fullText)
OrganizationCount(fullText)
print("-------------------------================")
print("-------------------------================")
print("-------------------------================")

gpe = get_chunks_with_its_labels(fullText,'GPE')
print(gpe)
print("-------------------------================")
print("-------------------------================")
print("-------------------------================")
freqdist = FreqDist(gpe).most_common()
print(freqdist)
print("-------------------------================")
print("-------------------------================")
print("-------------------------================")
person = get_chunks_with_its_labels(fullText,'PERSON')
print(person)
print("-------------------------================")
print("-------------------------================")
print("-------------------------================")
freqdist1 = FreqDist(person).most_common()
print(freqdist1)
print("-------------------------================")
print("-------------------------================")
print("-------------------------================")