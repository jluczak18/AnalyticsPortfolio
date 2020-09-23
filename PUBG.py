# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:13:57 2020

@author: jlucz
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#read in data
train = pd.read_csv('train_V2.csv')
test = pd.read_csv('test_V2.csv')

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

numVar = train.drop(['winPlacePerc', 'Id', 'groupId', 'matchId', 'matchType'], axis=1)
scaler.fit(numVar)

scaled_feat = pd.DataFrame(scaler.transform(numVar), columns=numVar.columns)

numVar.info()
scaled_feat.head()

boolVal = scaled_feat[(scaled_feat > 3) | (scaled_feat < -3)]
boolVal.head()

idx = pd.DataFrame()

for i in scaled_feat:
	sns.countplot(boolVal[boolVal[i].notnull() == True])
	
boolVal = (scaled_feat > 3) | (scaled_feat < -3)
boolVal['assists'].value_counts()

Outliers = 0

for i in scaled_feat:
	print(boolVal[i].value_counts())
	boolVal_i = boolVal[boolVal[i] == True].sum()
	Outliers = Outliers + boolVal_i
return Outliers
	

Outliers
boolVal['assists'][boolVal['assists'] == True].sum()

boolVal['assists'].value_counts()
scaled_feat.index(scaled_feat['assists'] > 3)


sns.heatmap(train.groupby('groupId').corr())
#understand the data further (exploratory data analysis)
#found a null value in winplaceperc when conducting further analysis
#need to remove one instance of null
train.info()

#create a heatmap to see if any variables have null values
sns.heatmap(train.isnull())

#remove the one null in winplaceperc
train['winPlacePerc'].isnull().sort_values(ascending=False)
train.drop([train.index[2744604]], inplace=True)

null_columns = train.columns[train.isnull().any()]


#Exploratory Analysis
sns.distplot(train['DBNOs'], bins=30)

train['longestKill'].describe()
#avg - 22 meters, std dev - 50 meters; 95% between 0 and 122

#makes sense that more downs lead to more kills as you have to down someone
#to kill them. What are these 0 downs and high kills? - Need to explore further
sns.scatterplot(x='DBNOs', y='kills', data=train)
train['DBNOs'].corr(train['kills'])

#create a variable to calculate total distance
train['totalDistance'] = train['walkDistance']+train['swimDistance']+train['rideDistance']
train[['walkDistance', 'swimDistance', 'rideDistance', 'totalDistance']].head()

sns.lmplot(x='weaponsAcquired', y='winPlacePerc', data=train)
#typically less walking results in more kills (campers)
sns.jointplot(x='kills', y='walkDistance', data=train)

#Picking up more items (getting better guns) doesn't result in 
#longer match time (aka getting to first place)
sns.jointplot(x='weaponsAcquired', y='matchDuration', data=train)

sns.lmplot(x='matchDuration', y='winPlacePerc', data=train)

#we have some categorical variables that won't work in a linear regression 
#equation so we need to make dummy variables. 
match = pd.get_dummies(train['matchType'], drop_first=True)
train.info()

#join the dummy variables with the original training data
#I created a new data set in case I need to make changes to the original
train_2 = pd.concat([train, match], axis=1)
train_2.info()

#using heatmap, we can look and see which values are correlated with
#the winPlacePerc. Those include: killPlace (neg correlation), walkDistance,
#boosts, weaponsacquired
plt.figure(figsize=(18,18))
sns.heatmap(train.corr(), cmap='coolwarm', linecolor='white', linewidth=.5, annot=True,
			fmt='.1f')

#walk distance is more heavily correlated than total distance
#don't think we can use both as they are heavily correlated with each other
#(multicollinearity)
train['winPlacePerc'].corr(train['totalDistance'])
train['winPlacePerc'].corr(train['walkDistance'])
train['totalDistance'].corr(train['walkDistance'])

sns.lmplot(x='kills', y='matchDuration', data=train_2,
		   hue='duo')

train_2.info()
train_2['longestKill']

#split the data into X (independent variables) and y (dependent variable) for
#regression equation 
X = train[['killPlace', 'boosts', 'walkDistance', 'weaponsAcquired']]
X.columns
X.info()
y=train['winPlacePerc']

#when running the fit of a regression line, we got an error with an input
#containing NaN, infinity, or value too large for dtype('float64')
#the IVs with float64 are walkDistance, 
#winPlacePerc
X.info()
sns.heatmap(X.isnull())
#There aren't any nulls in X

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.3)

from sklearn.linear_model import LinearRegression
linear = LinearRegression()
linear.fit(X_train, y_train)

predictions = linear.predict(X_test)

col = list(train.columns)
col = col[3:] #removes Id, groupID, and matchID which are categorical
col.remove('winPlacePerc')

col

for i in col:
	sns.scatterplot(x=i, y='winPlacePerc', data=train)
	plt.xlabel(i)
	plt.ylabel('winPlacePerc')
	plt.show()

X_test2 = test[['killPlace', 'boosts', 'walkDistance', 'weaponsAcquired']]
test_pred = linear.predict(X_test2)

results = pd.DataFrame(index=test['Id'], data=test_pred)
results.rename(columns={0:'winPlacePerc'}, inplace=True)
results.head()

sns.boxplot(y='boosts', data=train)
sns.boxplot(y='vehicleDestroys', data=train)


np.std(train['longestKill'])
np.mean(train['longestKill'])

np.mean(train['longestKill']) + 3*(np.std(train['longestKill']))

col = list(train.columns)
col = col[3:]
col.remove('winPlacePerc')
col.remove('matchType')

train.groupby('groupId').describe()

groupTrain = pd.DataFrame(train.groupby('groupId'))
