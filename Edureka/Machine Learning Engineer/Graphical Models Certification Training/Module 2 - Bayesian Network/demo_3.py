# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 04:07:06 2020

@author: SP
"""
from pgmpy.models import BayesianModel
import networkx as nx

model = BayesianModel()
model.add_nodes_from(['EMAIL CLIENT','SUSPICIOUS EMAIL LINK'])
model.add_edges_from([('EMAIL CLIENT','SUSPICIOUS EMAIL LINK'),('EMAIL CLIENT','SPAM KEYWORD')
                      ,('SPAM KEYWORD','SPAM EMAIL')
                      ,('SPECIAL CHARACTER','SPAM KEYWORD')])
nx.draw_networkx(model)