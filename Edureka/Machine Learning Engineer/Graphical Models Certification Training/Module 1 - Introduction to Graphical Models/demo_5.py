# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 00:54:10 2020

@author: SP
"""
import networkx as nx
from networkx.algorithms.approximation import clique
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from IPython.display import Image

''' Undirected Graphs '''
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3,4,5])
#nx.draw_networkx(G) #no edges
G.add_edge(1,2)
#nx.draw_networkx(G) #with edges
G.add_edges_from([(2,3),(3,4),(4,5)])
#nx.draw_networkx(G) #with edges
G.add_edge(1,3)
#nx.draw_networkx(G)
print(list(nx.find_cliques(G)))
print(clique.max_clique(G))

''' Directed Graphs '''
DiG = nx.DiGraph()
DiG.add_edges_from([('Burglar', 'Dog'), ('Burglar','Alarm'), ('Earthquake', 'Alarm'),
('Alarm','Police')])
#nx.draw_networkx(DiG)
#DiG.add_edge(1,3)
#nx.draw_networkx(DiG)
positions = {'Burglar':(2,6), 'Earthquake':(4,6), 'Alarm':(3,4), 'Dog':(1.5,3), 'Police':(3,1)}
#nx.draw_networkx(DiG,node_color='pink',node_size=15**3,font_size=20,arrowsize=40,pos=positions)
a = nx.to_pandas_adjacency(DiG)
print(a)
print(nx.to_pandas_edgelist(DiG))
#nx.draw_networkx(nx.DiGraph(a))

Image('779_m1_demo_5/graph.png')
bn = BayesianModel([('Burglar', 'Dog'), ('Burglar','Alarm'), ('Earthquake', 'Alarm'),
('Alarm','Police')])
nx.draw_networkx(bn)

cpd_Alarm = TabularCPD('Alarm', variable_card=2, values=[[0.98, 0.3, 0.4, 0.1],[0.02, 0.7, 0.6, 0.9]], evidence=['Earthquake','Burglar'], evidence_card=[2,2])
print(cpd_Alarm)

cpd_Police = TabularCPD('Police', variable_card=2, values=[[0.95, 0.02], [0.05, 0.98]],evidence=['Alarm'], evidence_card=[2])
cpd_Burglar = TabularCPD('Burglar', variable_card=2, values=[[0.5],[0.5]])
cpd_Earthquake = TabularCPD('Earthquake', 2, [[0.5],[0.5]])
cpd_Dog = TabularCPD('Dog', variable_card=2, values=([[0.8, 0.1], [0.2, 0.9]]),evidence=['Burglar'], evidence_card=[2])

bn.add_cpds(cpd_Police, cpd_Earthquake, cpd_Alarm, cpd_Burglar, cpd_Dog)
bn.check_model()
print(bn.get_cpds('Dog'))
print(bn.is_active_trail(start='Earthquake',end='Burglar'))
print(bn.get_independencies())