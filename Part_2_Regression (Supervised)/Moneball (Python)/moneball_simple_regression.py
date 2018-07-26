#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:59:15 2017

@author: pablo
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('baseball.csv')
dataset = dataset[dataset.Year < 2002]
dataset['RD'] = dataset['RS'] - dataset['RA']

# plotting RD vs W to see a relationship
dataset.plot.scatter(x = 'RD', y = 'W')

X = dataset.iloc[:,-1].values.reshape(-1, 1)
y = dataset.iloc[:,5].values.reshape(-1, 1)

X = np.array(X, dtype=float)
y = np.array(y, dtype=float)
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

import statsmodels.formula.api as sm
X = np.append(arr = np.ones(shape = (902, 1)), values = X, axis = 1)

regressor_OLS = sm.OLS(endog = y, exog = X).fit()
regressor_OLS.summary()

# Predicting the Test set results
y_pred = regressor.predict(X_test)


# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('RD vs W')
plt.xlabel('RD')
plt.ylabel('Winners')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


