# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 04:13:08 2020

@author: SP
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import svm

data = pd.read_csv("College.csv")
labelencoder = LabelEncoder()
standaradscaler = StandardScaler()

y = data["Private"]
X = data.iloc[:,2:]

y = labelencoder.fit_transform(data["Private"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

support_vector_machine = svm.SVC(kernel = 'linear')
support_vector_machine.fit(X_train,y_train)
predict = support_vector_machine.predict(X_test)
print("---------------------------------------------")
print("---------Linear SVM Model without Standarad Scalar---------------")
print("Accuracy: ",accuracy_score(predict,y_test))
print("Confusion Matrix: \n",confusion_matrix(predict,y_test))
print("Classification Report: \n",classification_report(predict,y_test))

X = standaradscaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

support_vector_machine = svm.SVC(kernel = 'linear')
support_vector_machine.fit(X_train,y_train)
predict = support_vector_machine.predict(X_test)
print("---------------------------------------------")
print("---------Linear SVM Model with Scalar---------------")
print("Accuracy: ",accuracy_score(predict,y_test))
print("Confusion Matrix: \n",confusion_matrix(predict,y_test))
print("Classification Report: \n",classification_report(predict,y_test))

support_vector_machine = svm.SVC(kernel = 'poly')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
grid_values = {'C':[0.1, 1, 100, 1000],'gamma':[1, 0.1, 0.01, 0.001, 0.0001]}
grid_clf_acc = GridSearchCV(support_vector_machine, param_grid = grid_values)
grid_clf_acc.fit(X_train,y_train)
predict = grid_clf_acc.predict(X_test)
print("---------------------------------------------")
print("---------Poly SVM Model---------------")
print("Accuracy: ",accuracy_score(predict,y_test))
print("Confusion Matrix: \n",confusion_matrix(predict,y_test))
print("Classification Report: \n",classification_report(predict,y_test))
# print best parameter after tuning 
print("Best Hyperparameter: ",grid_clf_acc.best_params_) 
  
# print how our model looks after hyper-parameter tuning 
print("Model after adding Hyperparameters: ",grid_clf_acc.best_estimator_) 

support_vector_machine = svm.SVC(kernel = 'rbf')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
grid_values = {'C':[0.1, 1, 10, 100, 1000],'gamma':[1, 0.1, 0.01, 0.001, 0.0001]}
grid_clf_acc = GridSearchCV(support_vector_machine, param_grid = grid_values)
grid_clf_acc.fit(X_train,y_train)
predict = grid_clf_acc.predict(X_test)
print("---------------------------------------------")
print("---------RBf SVM model---------------")
print("Accuracy: ",accuracy_score(predict,y_test))
print("Confusion Matrix: \n",confusion_matrix(predict,y_test))
print("Classification Report: \n",classification_report(predict,y_test))
# print best parameter after tuning 
print("Best Hyperparameter: ",grid_clf_acc.best_params_) 
  
# print how our model looks after hyper-parameter tuning 
print("Model after adding Hyperparameter: ",grid_clf_acc.best_estimator_) 
