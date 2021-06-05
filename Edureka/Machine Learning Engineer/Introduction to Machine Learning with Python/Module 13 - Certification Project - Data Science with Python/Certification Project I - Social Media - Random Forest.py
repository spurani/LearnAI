#Classification for Online News Popularity
#Importing the Libraries
import pandas as pd
#Importing the dataset
dataset = pd.read_csv('OnlineNewsPopularity.csv')
X = dataset.iloc[:,2:-2].values
Y = dataset.iloc[:, -1].values
#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
#Fitting Gradient Boosting to Training set
from sklearn.ensemble import GradientBoostingClassifier
classifier = GradientBoostingClassifier()
classifier.fit(X_train, Y_train)
#Predicting the Test set results
Y_pred = classifier.predict(X_test)
#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm)