# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:39:10 2020

@author: SP
"""
from pgmpy.factors.discrete import TabularCPD
from pgmpy.factors.discrete import JointProbabilityDistribution as JPD
cpd = TabularCPD('MarketPerformance',2,[[0.11,0.06],[0.29,0.54]],evidence=['Program'],evidence_card=[2])
print(cpd)
cpd = TabularCPD('grade',2,[[0.7,0.6,0.6,0.2],[0.3,0.4,0.4,0.8]],evidence=['intel','diff'],evidence_card=[2,2])
print(cpd)
print(cpd.variables)
print(cpd.cardinality)
prob =  JPD(['I','D','G'],[2,2,3],
[0.126,0.168,0.126,0.009,0.045,0.126,0.252,0.0224,0.0056,0.06,0.036,0.024])
print(prob)
print(prob.check_independence(['I'], ['D']))
print(prob.check_independence(['I'], ['G']))
print(prob.check_independence(['I'], ['D'], [('G',0)]))
print(prob.check_independence(['I'], ['D'], ('G',), condition_random_variable=True))
print(prob.get_independencies())