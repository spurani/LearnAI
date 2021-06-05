# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 05:58:58 2020

@author: SP
"""
import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
import matplotlib.pyplot as plt
import networkx as nx
claim_dataset_pt_1 = pd.read_csv("Datasets/Claim_Dataset_Part1.csv")
claim_dataset_pt_2 = pd.read_csv("Datasets/Claim_Dataset_Part2.csv")

#print(claim_dataset_pt_2)
data = claim_dataset_pt_1.loc[:,['Qty','Days','Strength','Gender','Age','EarlyRefill','Fraud']]
''' Construct Bayesian network by considering all possible attributes of a prescription '''
''' Perform parametric estimation of probabilities '''
model = BayesianModel()
model.add_edges_from([('Qty','Strength'),('Days','Strength'),('Qty','Days'),('Strength','Gender'),('Strength','Age'),('Gender','EarlyRefill'),('Age','EarlyRefill'),('EarlyRefill','Fraud')])
G = nx.DiGraph(model)
nx.draw(G,with_labels=True)
plt.show()
claims = BayesianModel([('Qty','Strength'),('Days','Strength'),('Qty','Days'),('Strength','Gender'),('Strength','Age'),('Gender','EarlyRefill'),('Age','EarlyRefill'),('EarlyRefill','Fraud')])
print(claims.nodes())
nx.draw_shell(claims,with_labels=True)
plt.show()
claims.fit(data, estimator=MaximumLikelihoodEstimator)
claims.get_cpds()

'''
Find out all events leading to a case of substance abuse with rare evidence
'''

claims.active_trail_nodes('Fraud')
claims.active_trail_nodes('Qty',observed ='Fraud')


'''How likely a PATIENT is to switch from LOW dose category to HIGH dose category (Change in supply/ Reduction in days/ Changed strength of drug?) '''
change_in_supply = claim_dataset_pt_1['PhID'].unique().tolist()
print("Chnage in Supply: " , len(change_in_supply))
reduction_in_days = claim_dataset_pt_1['Days'].unique().tolist()
print("Reduction in Days: " , len(reduction_in_days))
change_strength_of_drug = claim_dataset_pt_1['Strength'].unique().tolist()
print("Change in Strength of drug" , len(change_strength_of_drug))
print("Strenght States: " , change_strength_of_drug.sort(reverse=False))
print(change_strength_of_drug)

customer_frame_dosage = claim_dataset_pt_1[['PhID','PATID','DCID','Days','Strength']]
customer_frame_dosage_sorted = customer_frame_dosage.sort_values(['PATID', 'DCID', 'Strength'], ascending=[True, True, True])

claims_filtered = pd.DataFrame(columns=customer_frame_dosage_sorted.columns)
print("---")
print(claims_filtered)
print("---")


current_patientID = 0
current_drugID = 0
current_strength = 0.0
current_row = 0

print("customer_frame_dosage_sorted at Start: ", len(customer_frame_dosage_sorted),'\n')
print("claims_filtered at Start: ", len(claims_filtered), '\n')

for row in range(len(customer_frame_dosage_sorted)):
    if (current_patientID == customer_frame_dosage_sorted.loc[row,'PATID'] ):
#         if (current_drugID == customer_frame_dosage_sorted.loc[row,'DCID']):
        if (current_strength < customer_frame_dosage_sorted.loc[row,'Strength']):
            claims_filtered.loc[current_row] = customer_frame_dosage_sorted.iloc[row]
#             print("Source : ", customer_frame_dosage_sorted.iloc[row], '\n')
#             print("Filtered : ", claims_filtered.iloc[current_row], '\n')
#             print("Strength Current: ", current_strength, " New: ", customer_frame_dosage_sorted.loc[row,'Strength'] )
            current_row += 1
    current_patientID = customer_frame_dosage_sorted.loc[row,'PATID']
    current_drugID = customer_frame_dosage_sorted.loc[row,'DCID']
    current_strength = customer_frame_dosage_sorted.loc[row,'Strength']  
    
print("customer_frame_dosage_sorted at End: ", len(customer_frame_dosage_sorted),'\n')
print("claims_filtered at End: ", len(claims_filtered), '\n')

'''Create the state space and find the unique products'''
states = claim_dataset_pt_2['Fraud'].unique().tolist()
print(states)
size = len(states)
print(size)

'''Create possible sequence of transitions and transition matrix'''
'''Possible sequences of events'''
transitionName = [['N','Y'],['Y','Y'],['Y','N'],['N','N']]
'''Probrability matrix (transition matrix - an empty one)'''
transitionMatrix = np.zeros((size,size))
print(transitionMatrix)
pat_list = claim_dataset_pt_2['PATID'].unique().tolist()

'''updating the transition matrix.'''
for x in pat_list:
    single_pat = claim_dataset_pt_2.loc[claim_dataset_pt_2['PATID'] == x]
    fraud1 = "NA"
    for i in range(2,21):
        for j in range(0,len(single_pat)):
            num = single_pat.values[j,i]
            if(num == 1.0):
                if(fraud1 == "NA"):
                    fraud1 = single_pat.values[j,1]
                else:
                    fraud2 = single_pat.values[j,1]
                    if(fraud1 == "N" and fraud2 == "Y"):
                        transitionMatrix[0,0] = transitionMatrix[0,0] + 1
                    if(fraud1 == "Y" and fraud2 == "Y"):
                        transitionMatrix[0,0] = transitionMatrix[0,1] + 1
                    if(fraud1 == "Y" and fraud2 == "N"):
                        transitionMatrix[1,0] = transitionMatrix[1,0] + 1
                    if(fraud1 == "N" and fraud2 == "N"):
                        transitionMatrix[1,1] = transitionMatrix[1,1] + 1
                    fraud1 = fraud2
print(transitionMatrix)
transitionMatrix=(transitionMatrix.T/transitionMatrix.sum(axis=1)).T

def fraud_forecast(fraud_num):
    first_fraud = "N"
    print("First Fraud: " + first_fraud)
    fraudList = [first_fraud]
    i = 0
    prob = 1
    while 1 != fraud_num:
        if(first_fraud == "N"):
            change = np.random.choice(transitionMatrix[0],replace=True)
            if( change == "Y"):
                prob = prob * transitionMatrix[1,0]
                first_fraud = "Y"
                fraudList.append("Y")
                pass
            else:
                prob = prob * transitionMatrix[1,1]
                first_fraud = "N"
                fraudList.append("N")
        elif first_fraud == "Y":
            change = np.random.choice(transitionMatrix[0],replace=True)
            if(change == "N"):
                prob = prob * transitionMatrix[1,0]
                first_fraud = "N"
                fraudList.append("N")
                pass
            else:
                prob = prob * transitionMatrix[1,1]
                first_fraud = "Y"
                fraudList.append("Y")
        i += 1
    print("Possible states: " + str(fraudList))
    print("Probability of the possible sequence of states: " + str(prob))
#fraud_forecast(3)
