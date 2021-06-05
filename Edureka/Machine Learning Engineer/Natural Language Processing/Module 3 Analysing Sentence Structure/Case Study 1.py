# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 03:37:06 2021

@author: SP
"""

from nltk import word_tokenize,pos_tag,FreqDist,RegexpTokenizer,RegexpParser
import re

source = open("698_m3_datasets_v1.0/FIFAWorldCup2018.txt")
data = source.read()
#print(data)
data_tokenize = word_tokenize(data)
#print(data_tokenize)

def GetNMostFrequentNouns(takedata,num):
    nmostfrequentnouns = {}
    nmostfrequentnouns_k_v = []
    for token in takedata:
        for all_tokens in pos_tag([token]):
            #print(all_tokens)
            if(all_tokens[1].startswith('NN')):
                if(all_tokens[0] in nmostfrequentnouns.keys()):
                    nmostfrequentnouns[all_tokens[0]] += 1
                else:
                    nmostfrequentnouns.setdefault(all_tokens[0],1)
    sort_l = sorted(nmostfrequentnouns, key=nmostfrequentnouns.get, reverse=True)[:num]
    for i in sort_l:
        if(i in nmostfrequentnouns):
            nmostfrequentnouns_k_v.append((i,nmostfrequentnouns[i]))
    return nmostfrequentnouns_k_v
    
GetNMostFrequentNouns(data_tokenize,10)

def GetNMostFrequentVerbs(takedata,num):
    nmostfrequentverbs = {}
    nmostfrequentverbs_k_v = []
    for token in takedata:
        for all_tokens in pos_tag([token]):
            #print(all_tokens)
            if(all_tokens[1].startswith('VB')):
                if(all_tokens[0] in nmostfrequentverbs.keys()):
                    nmostfrequentverbs[all_tokens[0]] += 1
                else:
                    nmostfrequentverbs.setdefault(all_tokens[0],1)
    sort_l = sorted(nmostfrequentverbs, key=nmostfrequentverbs.get, reverse=True)[:num]
    for i in sort_l:
        if(i in nmostfrequentverbs):
            nmostfrequentverbs_k_v.append((i,nmostfrequentverbs[i]))
    return nmostfrequentverbs_k_v
    
GetNMostFrequentVerbs(data_tokenize,10)

def GetNMostFrequentDelimiters(takedata,num):
    nmostfrequentdelimiters = {}
    nmostfrequentdelimiters_k_v = []
    delimiters = [' ',',',';',"'"]
    for token in takedata:
        for all_tokens in pos_tag([token]):
            #print(all_tokens)
            if(all_tokens[0] in delimiters):
                if(all_tokens[0] in nmostfrequentdelimiters.keys()):
                    nmostfrequentdelimiters[all_tokens[0]] += 1
                else:
                    nmostfrequentdelimiters.setdefault(all_tokens[0],1)
    sort_l = sorted(nmostfrequentdelimiters, key=nmostfrequentdelimiters.get, reverse=True)[:num]
    for i in sort_l:
        if(i in nmostfrequentdelimiters):
            nmostfrequentdelimiters_k_v.append((i,nmostfrequentdelimiters[i]))
    #print(nmostfrequentdelimiters_k_v)
    return nmostfrequentdelimiters_k_v
    
GetNMostFrequentDelimiters(data_tokenize,10)

def GetNMostFrequentPrepositions(takedata,num):
    freqdist = FreqDist()
    nmostfrequentprepositions = {}
    nmostfrequentprepositions_k_v = []
    for token in takedata:
        for all_tokens in pos_tag([token]):
            #print(all_tokens)
            if(all_tokens[1].startswith('IN')):
                freqdist[all_tokens] += 1
                if(all_tokens[0] in nmostfrequentprepositions.keys()):
                    nmostfrequentprepositions[all_tokens[0]] += 1
                else:
                    nmostfrequentprepositions.setdefault(all_tokens[0],1)
    sort_l = sorted(nmostfrequentprepositions, key=nmostfrequentprepositions.get, reverse=True)[:num]
    for i in sort_l:
        if(i in nmostfrequentprepositions):
            nmostfrequentprepositions_k_v.append((i,nmostfrequentprepositions[i]))
    #print(freqdist.most_common(10))
    return nmostfrequentprepositions_k_v
    
GetNMostFrequentPrepositions(data_tokenize,10)

def TextAfterRemovingPunctuations(takedata):
        res = re.sub(r'[^\w\s]', '', takedata)
        #print(res)
        return res

TextAfterRemovingPunctuations(data)

def TextAfterRemovingDigits(takedata):
        res = re.sub(r'\d','',takedata)
        return(res)
        
TextAfterRemovingDigits(data)

def AllCapitalizedWordsFromText(takedata):
        caps = takedata.upper()
        return caps

AllCapitalizedWordsFromText(data)

def AllEmailsFromText(takedata):
        email = re.match("[^(\d|A-Za-z)@*.com]",takedata)
        return email
AllCapitalizedWordsFromText(data)

def ChunkingVer1(takedata):
    grammer_np = r"NP: {<NP><VB>}"
    chunk_parser = RegexpParser(grammer_np)
    chunk_result = chunk_parser.parse(takedata)
    #print(chunk_result)
    return chunk_result
ChunkingVer1(pos_tag(data_tokenize))

def ChunkingVer2(takedata):
    grammer_np = r"NP: {<VB><JJ>}"
    chunk_parser = RegexpParser(grammer_np)
    chunk_result = chunk_parser.parse(takedata)
    #print(chunk_result)
    return chunk_result
ChunkingVer2(pos_tag(data_tokenize))


def ChunkingVer3(takedata):
    grammer_np = r"NP: {<VB><JJ>}"
    chunk_parser = RegexpParser(grammer_np)
    chunk_result = chunk_parser.parse(takedata)
    print(chunk_result)
    return chunk_result
ChunkingVer3(pos_tag(data_tokenize))

def ChunkingVer4(takedata):
    grammer_np = r"NP: {<DT><NN>}"
    chunk_parser = RegexpParser(grammer_np)
    chunk_result = chunk_parser.parse(takedata)
    print(chunk_result)
    return chunk_result
ChunkingVer4(pos_tag(data_tokenize))

def ChunkingVer5(takedata):
    grammer_np = r"NP: {<JJ><NN>}"
    chunk_parser = RegexpParser(grammer_np)
    chunk_result = chunk_parser.parse(takedata)
    print(chunk_result)
    return chunk_result
ChunkingVer5(pos_tag(data_tokenize))

