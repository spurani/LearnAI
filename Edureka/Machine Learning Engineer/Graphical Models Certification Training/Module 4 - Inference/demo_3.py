# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:19:29 2020

@author: SP
"""
from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel
from pgmpy.inference import GibbsSampling
import networkx as nx

model = BayesianModel()
model.add_nodes_from(['TRAFFIC','MILEAGE'])
model.add_nodes_from(['CATEGORY','MILEAGE'])
model.add_nodes_from(['CATEGORY','PERFORMANCE'])
model.add_nodes_from(['MILEAGE','REVIEW'])
model.add_edges_from([('TRAFFIC','MILEAGE'),('CATEGORY','MILEAGE'),('CATEGORY','PERFORMANCE'),('MILEAGE','REVIEW')])
nx.draw_networkx(model)
cpd_traffic = TabularCPD('TRAFFIC',2,[[0.7],[0.3]])
print(cpd_traffic)
cpd_category = TabularCPD('CATEGORY',2,[[0.6],[0.4]])
print(cpd_category)
cpd_mileage = TabularCPD('MILEAGE',3,[[0.2, 0.05, 0.9, 0.3],[0.6, 0.25, 0.08, 0.5],[0.2, 0.7, 0.02, 0.2]],['CATEGORY','TRAFFIC'],[2,2])
print(cpd_mileage)
cpd_p = TabularCPD('PERFORMANCE',2,[[0.95, 0.2],[0.05, 0.8]],['CATEGORY'],[2])
print(cpd_p)
cpd_review = TabularCPD('REVIEW',2,[[0.8,0.9,0.7],[0.2,0.1,0.3]],['MILEAGE'],[3])
print(cpd_review)
model.add_cpds(cpd_traffic,cpd_category,cpd_mileage,cpd_review,cpd_p)
print(model.check_model())