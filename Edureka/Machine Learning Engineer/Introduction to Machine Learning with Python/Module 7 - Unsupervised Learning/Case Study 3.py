# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 06:31:15 2020

@author: SP
"""
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.metrics import mean_squared_error, accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, normalize 
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("zoo.csv")
print(data.head())

uni_class_type = np.unique(data['class_type'])
data = data.drop('animal_name',axis=1)
print(uni_class_type)

scaler = StandardScaler() 
X_scaled = scaler.fit_transform(data) 
  
# Normalizing the data so that the data approximately  
# follows a Gaussian distribution 
X_normalized = normalize(X_scaled) 
  
# Converting the numpy array into a pandas DataFrame 
X_normalized = pd.DataFrame(X_normalized) 

pca = PCA(n_components = 2)
main_data = pca.fit_transform(X_normalized) 
main_data = pd.DataFrame(main_data) 
main_data.columns = ['P1', 'P2'] 

plt.figure(figsize=(10, 7))
plt.title("Zoo Dendograms")
dend = shc.dendrogram(shc.linkage(main_data, method='ward'))
features = data.iloc[:,1:16]

clustering = AgglomerativeClustering(n_clusters=3)
plt.figure(figsize = (10, 7))
plt.scatter(main_data['P1'], main_data['P2'], c = clustering.fit_predict(main_data), cmap = 'rainbow')

X = data.iloc[:,1:15].columns

train, test = train_test_split(data,test_size=0.3)
train_features = data.iloc[:80,:-1]
test_features = data.iloc[80:,:-1]
train_targets = data.iloc[:80,-1]
test_targets = data.iloc[80:,-1]

train_features = train[X]
test_features = test[X]

train_targets = train['class_type']
test_targets = test['class_type']

###########################################################################################################

##########################################################################################################


"""
Train the model
"""

tree = DecisionTreeClassifier(criterion = 'entropy').fit(train_features,train_targets)

###########################################################################################################

##########################################################################################################

"""
Predict the classes of new, unseen data
"""
prediction = tree.predict(test_features)


###########################################################################################################

##########################################################################################################

"""
Check the accuracy
"""
print("Classification Report \n: ",classification_report(prediction,test_targets))
print("Confusion Matrix \n: ",confusion_matrix(prediction,test_targets))
print("The prediction accuracy is: ",tree.score(test_features,test_targets)*100,"%")
print("Mean Squared Error",mean_squared_error(prediction,test_targets))