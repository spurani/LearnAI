# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:15:44 2020

@author: SP
"""
import networkx as nx
import numpy as np
from pgmpy.models import MarkovModel, BayesianModel
from pgmpy.factors.discrete import DiscreteFactor

# G = MarkovModel()
# G.add_node('a')
# G.add_edge('a','b')
# G.add_edges_from([('a','b'),('b','c')])
# print('a' in G)
# print(len(G))
# nx.draw_networkx(G)

'''Part II'''
mm = MarkovModel()
mm.add_nodes_from(['Joey','Rachel','Monica','Ross','Chandler','Stefan','Philip'])
mm.add_edges_from([('Joey', 'Rachel'), ('Joey', 'Stefan'), ('Joey','Philip'),
 ('Rachel', 'Monica'), ('Rachel', 'Stefan'), ('Rachel', 'Philip'),
 ('Monica', 'Ross'), ('Monica', 'Chandler'), ('Ross', 'Chandler'), ('Chandler','Philip')])
# nx.draw_networkx(mm)
print(mm.get_local_independencies())
bm = mm.to_bayesian_model()
nx.draw_networkx(bm)
phi = [DiscreteFactor(edge,[2,2],np.random.rand(4)) for edge in mm.edges()]
mm.add_factors(*phi)
mm.get_cardinality()
print(mm.get_cardinality(node='Rachel'))
print(mm.get_factors(node='Rachel'))
print(mm.get_factors())
print(mm.get_partition_function())
for dd in mm.markov_blanket('Chandler'):
    print(dd)
factor_graph = mm.to_factor_graph()
nx.draw_networkx(factor_graph)
