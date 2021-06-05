# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:13:15 2020

@author: SP
"""
import pandas as pd
from numpy import mean
from numpy import std
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit,GridSearchCV, RepeatedKFold,cross_val_score
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix, classification_report,accuracy_score
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
data = pd.read_csv("OnlineNewsPopularity.csv")
#print(data.columns)
print(data.isnull().sum().sum())
x = data.iloc[:,1:-1]
# x = data.loc[:,[
#        'timedelta', 'n_tokens_title', 'n_tokens_content',
#        'num_hrefs', 'num_self_hrefs', 'num_imgs', 'num_videos',
#        'average_token_length', 'num_keywords', 'data_channel_is_lifestyle',
#        ' data_channel_is_entertainment', 'data_channel_is_bus',
#        'data_channel_is_socmed', 'data_channel_is_tech',
#        'data_channel_is_world', 'kw_min_min',
#        'kw_min_max', 'kw_max_max', 'kw_avg_max', 'kw_min_avg',
#        'self_reference_min_shares',
#        'weekday_is_monday', 'weekday_is_tuesday',
#        'weekday_is_wednesday', 'weekday_is_thursday', 'weekday_is_friday',
#        'weekday_is_saturday','LDA_00',
#        'LDA_01', 'LDA_02', 'LDA_03', 'LDA_04', 'global_subjectivity',
#        'global_sentiment_polarity', 'global_rate_positive_words',
#        'global_rate_negative_words', 'rate_positive_words',
#        'rate_negative_words', 'avg_positive_polarity', 'min_positive_polarity',
#        'max_positive_polarity',
#        'max_negative_polarity', 'title_subjectivity',
#        'title_sentiment_polarity', 'abs_title_subjectivity',
#        'abs_title_sentiment_polarity']]
y = data["shares"]
prediction_var = x.columns
# coorelations = data.corr()
# plt.figure(figsize=(50,50))
# sns.heatmap(coorelations, square = True, cmap = 'YlGnBu', annot=True)
# plt.yticks(rotation = 0)
# plt.xticks(rotation = 90)
# plt.show()
'''
def select_features(X_train, y_train, X_test):
	# configure to select all features
	fs = SelectKBest(score_func=mutual_info_regression, k=10)
	# learn relationship from training data
	fs.fit(X_train, y_train)
	# transform train input data
	X_train_fs = fs.transform(X_train)
	# transform test input data
	X_test_fs = fs.transform(X_test)
	return X_train_fs, X_test_fs, fs
 '''
# load the dataset
# split into train and test sets
#X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)
# feature selection
'''X_train_fs, X_test_fs, fs = select_features(X_train, y_train, X_test)
# what are scores for the features
for i in range(len(fs.scores_)):
 	print('Feature %d: %f' % (i, fs.scores_[i]))
# plot the scores
plt.bar([i for i in range(len(fs.scores_))], fs.scores_)
plt.show()

lm = LinearRegression()
model = lm.fit(X_train, y_train)
pred_y = lm.predict(X_test)
# The coefficients
print('Coefficients: \n', lm.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, pred_y))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, pred_y))

# Plot outputs
plt.scatter(y_test, pred_y,  color='black')
#plt.plot(x_test, pred_y, color='blue', linewidth=3)

plt.show()
'''

'''
Classification
'''
# train, test = train_test_split(data, test_size = 0.3)
# X_train = train[prediction_var]
# y_train = train['shares']
# X_test = test[prediction_var]
# y_test = test['shares']
# model = DecisionTreeClassifier()
# model.fit(X_train,y_train)# now fit our model for traiing data
# prediction=model.predict(X_test)
# df=pd.DataFrame(prediction,y_test)
# print(accuracy_score(prediction,y_test))

'''
Random Forest Classifier
'''
# trainedforest = RandomForestClassifier(n_estimators=700).fit(X_train,y_train)
# predictionforest = trainedforest.predict(X_test)
# print(confusion_matrix(y_test,predictionforest))
# print(classification_report(y_test,predictionforest))