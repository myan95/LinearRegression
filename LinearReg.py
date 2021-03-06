# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 03:19:52 2017

@author: Nancy Sherif IME
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('LungCap_Age.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.cross_validation import train_test_split 
X_train ,X_test ,y_train , y_test = train_test_split(X,y,test_size = 1/3 , random_state =0)

from sklearn.linear_model import LinearRegression 
regressor = LinearRegression()
regressor.fit(X_train , y_train)
 
 
y_pred = regressor.predict(X_test)

plt.scatter(X_train , y_train , color = 'red')
plt.plot(X_train , regressor.predict(X_train), color = 'blue')
plt.title('LungCap, Age training set')
plt.xlabel('LungCap')
plt.ylabel('Age')
plt.show()

plt.scatter(X_test , y_test , color = 'red')
plt.plot(X_train , regressor.predict(X_train), color = 'blue')
plt.title('LungCap, Age training set')
plt.xlabel('LungCap')
plt.ylabel('Age')
plt.show()
