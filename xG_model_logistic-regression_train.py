# -*- coding: utf-8 -*-
"""
@author: Michael
"""

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import pickle
import parameters


###
### LOAD & SHAPE THE DATA
###

# set the location of the file with the seed data
shots_training_seasons = 'shots_train.csv'

# create a dataframe of the seed data; duplicate it and drop unneeded columns
shots_train_df = pd.read_csv(shots_training_seasons)
shots_df = shots_train_df.copy()
shots_df = shots_df.drop(columns=parameters.drop_columns)


###
### LOGISTIC REGRESSION
###

# set the independent variables
continuous_variables = parameters.continuous_variables
boolean_variables = parameters.boolean_variables
independent_variables = continuous_variables + boolean_variables
x = shots_df[independent_variables]

# set the dependent variable
y = shots_df['IS_GOAL']

# apply the logistic regression
logreg = LogisticRegression(solver='sag', random_state=42, tol=.01, max_iter=10000)

# create regularization hyperparameter space
C = [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]

# create hyperparameter options
hyperparameters = dict(C=C, penalty=['l2'])

# create grid search
clf = GridSearchCV(logreg, hyperparameters, cv=10, verbose=10)

# fit grid search
clf.fit(x, y)

print("\nLogistic Regression Classifier:\n", clf)

# save model
pickle.dump(clf, open("pickle_logreg.pkl", 'wb'))
