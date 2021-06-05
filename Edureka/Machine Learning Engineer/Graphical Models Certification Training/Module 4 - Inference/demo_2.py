# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:54:16 2020

@author: SP
"""
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination,BeliefPropagation
from pgmpy.factors.discrete import TabularCPD
import networkx as nx
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

model = BayesianModel([('TRAFFIC','MILEAGE'),('CATEGORY','MILEAGE'),('CATEGORY','PERFORMANCE'),('MILEAGE','REVIEW')])
print("NODES: ",model.nodes(),end="\n")
print("EDGES: ",model.edges(),end="\n")
cpd_t = TabularCPD('TRAFFIC',2,[[0.6],[0.4]])
cpd_c = TabularCPD('CATEGORY',2,[[0.7],[0.3]])
cpd_mileage = TabularCPD('MILEAGE',3,[[0.2, 0.05, 0.9, 0.3],
 [0.6, 0.25, 0.08, 0.5],
 [0.2, 0.7, 0.02, 0.2]],['CATEGORY','TRAFFIC'],[2,2])
cpd_p = TabularCPD('PERFORMANCE',2,[[0.95, 0.2],
 [0.05, 0.8]],['CATEGORY'],[2])
cpd_r = TabularCPD('REVIEW',2,[[0.1, 0.4, 0.99],
 [0.9, 0.6, 0.01]],['MILEAGE'],[3])
model.add_cpds(cpd_t,cpd_c,cpd_mileage,cpd_r,cpd_p)
print(model.check_model())
G = nx.DiGraph(model)
nx.draw(G,with_labels=True)
model_inference = VariableElimination(model)
print(model_inference.query(variables=['MILEAGE'],evidence={'TRAFFIC':0,'CATEGORY':0}))
model_inference_belief_propagation = BeliefPropagation(model)
print(model_inference_belief_propagation.query(variables=['MILEAGE'],evidence={'TRAFFIC':0,'CATEGORY':1}))
print(model_inference_belief_propagation.map_query(variables=['MILEAGE'],evidence={'TRAFFIC':1,'CATEGORY':1}))