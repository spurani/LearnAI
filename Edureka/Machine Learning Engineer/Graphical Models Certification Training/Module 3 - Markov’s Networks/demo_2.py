# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 06:05:56 2020

@author: SP
"""
import pandas as pd
from pgmpy.models import MarkovChain as MC
import numpy as np

data = pd.read_csv('779_m3_demo_2/Markov_Data.csv')
print(data)