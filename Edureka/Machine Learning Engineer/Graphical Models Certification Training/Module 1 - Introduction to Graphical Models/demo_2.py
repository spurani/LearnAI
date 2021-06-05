# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:34:37 2020

@author: SP
"""
import pandas as pd
data = pd.read_csv("779_m1_demo_2/Purchase Behavior.csv")
data = data.groupby(['Gender','Age','Purchased']).size()/400
print(data)