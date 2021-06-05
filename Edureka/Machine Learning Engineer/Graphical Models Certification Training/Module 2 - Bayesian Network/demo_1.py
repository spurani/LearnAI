# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:52:48 2020

@author: SP
"""
import matplotlib.pyplot as plt
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
import networkx as nx

model_b = BayesianModel()
model_b.add_nodes_from(['SMOG','TRAFFIC'])
model_b.add_edge('SMOG','TRAFFIC')
print(model_b.nodes())
print(model_b.edges())
model_b.add_edge('ACCIDENT','TRAFFIC')
model_b.add_edges_from(
[('WOKE_LATE', 'LATE_TO_OFFICE'),
('TRAFFIC', 'LATE_TO_OFFICE')])
print(model_b.nodes())
print(model_b.edges())
cpd_smog = TabularCPD('SMOG',2,[[0.4],[0.6]])
cpd_accident = TabularCPD('ACCIDENT',2,[[0.2],[0.8]])
cpd_traffic = TabularCPD('TRAFFIC',2,[[0.9,0.6,0.7,0.1],[0.1,0.4,0.3,0.9]],evidence=['SMOG','ACCIDENT'],evidence_card=[2,2])
print("CPD of Smog",cpd_smog,end="\n")
print("CPD of Accident",cpd_accident,end="\n")
print("CPD of Traffic Jam",cpd_traffic,end="\n")
nx.draw_shell(model_b,with_labels=True)
model_b.add_cpds(cpd_smog,cpd_accident,cpd_traffic)
#print(model_b.get_cpds())
cpd_woke_late = TabularCPD('WOKE_LATE',2,[[0.6],[0.4]])
cpd_late_to_office = TabularCPD('LATE_TO_OFFICE',2,[[0.9,0.45,0.8,0.1],[0.1,0.55,0.2,0.9]],evidence=['WOKE_LATE','TRAFFIC'],evidence_card=[2,2])
model_b.add_cpds(cpd_woke_late,cpd_late_to_office)
print(model_b.get_cpds())
print(model_b.check_model())
import warnings
warnings.filterwarnings("ignore")
import networkx as nx
nx.draw_shell(model_b,with_labels=True)