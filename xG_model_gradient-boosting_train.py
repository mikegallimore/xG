# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
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
### FIT A GRADIENT BOOSTING ALGORITHM
###

# set the independent variables
continuous_variables = parameters.continuous_variables
boolean_variables = parameters.boolean_variables
independent_variables = continuous_variables + boolean_variables
x = shots_df[independent_variables]

# set the dependent variable
y = shots_df['IS_GOAL']

# create the classifier
clf = GradientBoostingClassifier(n_estimators=250, learning_rate=.1, random_state=42, verbose=10)

# create hyperparameter options
param_grid = {'min_samples_split': [100, 250, 500], 'max_depth': [3]}

# create grid search
cv = GridSearchCV(estimator=clf, param_grid=param_grid, cv=10)

# fit grid search
cv.fit(x, y)

print("\nGradient Boosting Classifier:\n", cv)

# save model
pickle.dump(cv, open("pickle_gb.pkl", 'wb'))
