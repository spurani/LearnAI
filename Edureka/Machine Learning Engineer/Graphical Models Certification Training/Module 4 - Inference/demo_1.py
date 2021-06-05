# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 04:35:38 2020

@author: SP
"""
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD
import warnings
import matplotlib.pyplot as plt
import networkx as nx
warnings.filterwarnings("ignore")

model = BayesianModel([('LOCATION','INTERNET SPEED'),('NETWORK TYPE','INTERNET SPEED'),('DATA PACKS','NUMBER OF CUSTOMERS'),('INTERNET SPEED','NUMBER OF CUSTOMERS')])
print("NODES: ",model.nodes(),end="\n")
print("EDGES: ",model.edges(),end="\n")
cpd_location = TabularCPD('LOCATION',2,[[0.7],[0.3]])
cpd_network_type = TabularCPD('NETWORK TYPE',2,[[0.6],[0.4]])
cpd_speed = TabularCPD('INTERNET SPEED',2,[[0.8, 0.6, 0.6, 0.3],[0.2, 0.4, 0.4, 0.7]],['LOCATION','NETWORK TYPE'],[2,2])
cpd_data_packs = TabularCPD('DATA PACKS',2,[[0.6], [0.4]])
cpd_no_of_customers = TabularCPD('NUMBER OF CUSTOMERS',2,[[0.9,0.5,0.7,0.1],[0.1,0.5,0.3,0.9]],['INTERNET SPEED','DATA PACKS'],[2,2])
model.add_cpds(cpd_location, cpd_network_type, cpd_speed, cpd_data_packs, cpd_no_of_customers)
print(cpd_no_of_customers)
print(cpd_data_packs)
print(cpd_location)
print(cpd_network_type)
print(cpd_speed)
print(model.check_model())
print(model.local_independencies(['DATA PACKS','LOCATION','INTERNET SPEED','NUMBER OF CUSTOMERS','NETWORK TYPE']))
G = nx.DiGraph(model)
print(nx.draw_shell(G,with_labels=True))
model_inference = VariableElimination(model)
print(model_inference.query(variables=['LOCATION']))
print(model_inference.query(variables=['NUMBER OF CUSTOMERS']))
print(model_inference.query(variables=['LOCATION','NUMBER OF CUSTOMERS']))
print(model_inference.query(variables=['NUMBER OF CUSTOMERS'],elimination_order=['LOCATION','INTERNET SPEED','NETWORK TYPE']))
print(model_inference.query(variables=['NUMBER OF CUSTOMERS'],evidence={'LOCATION':0}))
print(model_inference.query(variables=['NUMBER OF CUSTOMERS'],evidence={'LOCATION':1}))
print(model_inference.query(variables=['NUMBER OF CUSTOMERS'],
 evidence={'LOCATION': 1, 'NETWORK TYPE': 0}))
print(model_inference.map_query(variables=['NUMBER OF CUSTOMERS'],
 evidence={'LOCATION': 1, 'NETWORK TYPE': 0}))
induced_graph1 = model_inference.induced_graph(['DATA PACKS','LOCATION','INTERNET SPEED','NUMBER OF CUSTOMERS','NETWORK TYPE'])
nx.draw_shell(induced_graph1,with_labels=True)