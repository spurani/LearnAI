# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 07:22:51 2020

@author: SP
"""
from pgmpy.factors.discrete import DiscreteFactor
from pgmpy.models import FactorGraph
import networkx as nx
phi = DiscreteFactor(['A','B'],[2,2],[100,1,5,1000])
print(phi)
print(phi.scope())
G = FactorGraph()
G.add_nodes_from(['A', 'B'])
G.add_factors(phi)
G.add_nodes_from([phi])
G.add_edges_from([('A',phi),('B',phi)])
mm = G.to_markov_model()
nx.draw_networkx(G,pos=nx.spring_layout(G))

phi_marginalized = phi.marginalize(['A'], inplace= False)
print(phi_marginalized)
phi_reduction = phi.reduce([('A',0)], inplace = False)
print(phi_reduction)