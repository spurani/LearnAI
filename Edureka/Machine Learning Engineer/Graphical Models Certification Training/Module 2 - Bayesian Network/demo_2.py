# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 01:46:45 2020

@author: SP
"""
from pgmpy.models import BayesianModel
import networkx as nx
from pgmpy.factors.discrete import TabularCPD

model = BayesianModel()
model.add_nodes_from(['GENDER','SUCCESS'])
model.add_edges_from([('GENDER','SUCCESS'),('AGE GROUP','MARTIAL STATUS'),('AGE GROUP','SUCCESS'),('MARTIAL STATUS','SUCCESS')])
model.add_edge('BUSINESS','EMPLOYED')
model.add_edge('EMPLOYED','SUCCESS')
cpd_age_group = TabularCPD('AGE GROUP',2,[[0.4],[0.6]])
print(cpd_age_group)
cpd_employment_status = TabularCPD('EMPLOYED',2,[[0.55,0.65],[0.35,0.30]],evidence=['BUSINESS'],evidence_card=[2])
print(cpd_employment_status)
cpd_gender = TabularCPD('GENDER',2,[[0.2],[0.19]])
print(cpd_gender)
cpd_martial_status = TabularCPD('MARTIAL STATUS',2,[[0.25,0.18],[0.65,0.95]],evidence=['AGE GROUP'],evidence_card=[2])
print(cpd_martial_status)
cpd_business = TabularCPD('BUSINESS',2,[[0.67],[0.33]])
print(cpd_business)
cpd_success = TabularCPD('SUCCESS',2,[[1, 0.85, 0.65, 0.12, 0.95, 0.8, 0.95, 0.4, 0.05, 0.9, 0.6, 0.7, 0.8, 0.5, 0.9, 0.02],[0, 0.15, 0.35, 0.88, 0.05, 0.2, 0.05, 0.6, 0.95, 0.1, 0.4, 0.3, 0.2, 0.5, 0.1, 0.98]],evidence=['GENDER','AGE GROUP','MARTIAL STATUS','EMPLOYED'],evidence_card=[2,2,2,2])
print(cpd_success)
model.add_cpds(cpd_age_group,cpd_employment_status,cpd_gender,cpd_martial_status,cpd_business)
print(model.get_cpds())
print(model.check_model)
#print(model.get_independencies('SUCCESS'))
print(model.local_independencies('SUCCESS'))
#nx.draw_networkx(model)