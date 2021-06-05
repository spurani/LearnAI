# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 19:24:31 2020

@author: SP
"""
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb

diag = gum.InfluenceDiagram()
print(diag)

t = diag.addChanceNode(gum.LabelizedVariable('T','Traffic',2))
m = diag.addChanceNode(gum.LabelizedVariable('M','Mileage',3))
c = diag.addChanceNode(gum.LabelizedVariable('C','Category',2))
p = diag.addChanceNode(gum.LabelizedVariable('P','Performance',2))
r = diag.addChanceNode(gum.LabelizedVariable('R','Review',2))
b = diag.addDecisionNode(gum.LabelizedVariable('B','Buy',2))
s = diag.addUtilityNode(gum.LabelizedVariable("S","Satisfaction",1))
diag.addArc(diag.idFromName('T'),diag.idFromName('M'))
diag.addArc(diag.idFromName('C'),diag.idFromName('M'))
diag.addArc(diag.idFromName('M'),diag.idFromName('R'))
diag.addArc(diag.idFromName('C'),diag.idFromName('P'))
diag.addArc(diag.idFromName('R'),diag.idFromName('B'))
diag.addArc(diag.idFromName("B"),s)
diag.addArc(diag.idFromName("P"),s)
gnb.showInfluenceDiagram(diag,size="6")
diag.cpt(t).fillWith([0.6,0.4])
diag.cpt(c).fillWith([0.7,0.3])
diag.cpt(m).var_names
diag.cpt(m)[0,0,:] = [0.2,0.6,0.2]
diag.cpt(m)[0,1,:] = [0.05,0.25,0.7]
diag.cpt(m)[1,0,:] = [0.9,0.08,0.02]
diag.cpt(m)[ 1, 1,:] = [0.3,0.5,0.2]
print(diag.cpt(m))