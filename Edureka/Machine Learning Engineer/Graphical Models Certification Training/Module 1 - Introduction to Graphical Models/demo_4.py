# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 23:10:04 2020

@author: SP
"""
import numpy as np
import pandas as pd

class BayesTable(pd.DataFrame):
    def __init__(self, hypo, prior = 1):
        columns = ['hypo','prior','likelihood','unnorm','posterior']
        super().__init__(columns = columns)
        self.hypo = hypo
        self.prior = prior
    def mult(self):
        self.unnorm = self.prior * self.likelihood
    def norm(self):
        nc = np.sum(self.unnorm)
        self.posterior = self.unnorm / nc
        return nc
    def update(self):
        self.mult()
        return self.norm()
    def reset(self):
        return BayesTable(self.hypo, self.posterior)

table = BayesTable(['Urn 1','Urn 2'])
print(table)
table.likelihood = [3/4,1/2]
print(table)
table.mult()
print(table)
table.norm()
print(table)