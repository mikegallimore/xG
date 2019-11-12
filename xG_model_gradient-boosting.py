# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:42:14 2019

@author: Michael
"""
###
### IMPORT NEEDED PACKAGES
###

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
import pickle

###
### LOAD & SHAPE THE DATA
###

### set the location of the file with the seed data
shots_training_seasons = 'shots_train.csv'

### create a dataframe of the seed data; duplicate it and drop unneeded columns
shots_df = pd.read_csv(shots_training_seasons)
xg_df = shots_df.copy()
xg_df = xg_df.drop(columns=['SEASON', 'GAME_ID', 'HOME', 'AWAY', 'HOME_GOALS', 'AWAY_GOALS', 'HOME_SCOREDIFF', 'AWAY_SCOREDIFF', 'HOME_SITUATION', 'AWAY_SITUATION', 'HOME_ZONE', 'AWAY_ZONE', 'X_1', 'Y_1'])


###
### FIT A GRADIENT BOOSTING ALGORITHM
###

### set the independent variables
continuous_variables = ['SECONDS_LAST_EVENT', 'X_ADJ', 'Y_ADJ', 'ANGLE', 'DISTANCE', 'DISTANCE_LAST_EVENT']
boolean_variables = ['IS_SHOOTER_POS_F', 'IS_TEAM_HOME', 'IS_ON_NET', 'IS_REBOUND', 'IS_A_NET_EMPTY', 'IS_TEAM_UP_3_OR_MORE', 'IS_TEAM_UP_2', 'IS_TEAM_UP_1', 'IS_TEAM_TIED', 'IS_TEAM_DOWN_1', 'IS_TEAM_DOWN_2', 'IS_TEAM_DOWN_3_OR_MORE', 'IS_TEAM_5v5', 'IS_TEAM_4v4', 'IS_TEAM_3v3', 'IS_TEAM_5v4', 'IS_TEAM_5v3', 'IS_TEAM_4v3', 'IS_TEAM_4v5', 'IS_TEAM_3v5', 'IS_TEAM_3v4']
independent_variables = continuous_variables + boolean_variables
x = xg_df[independent_variables]

### set the dependent variable
y = xg_df['IS_GOAL']

### create the classifier
clf = GradientBoostingClassifier(n_estimators=500, learning_rate=.1, random_state=42, verbose=10)

### create hyperparameter options
param_grid = {'min_samples_split': [100, 250, 500], 'max_depth': [3, 4, 5]}

### create grid search
cv = GridSearchCV(estimator=clf, param_grid=param_grid, cv=10)

### fit grid search
clf.fit(x, y)

print("\nGradient Boosting Classifier:\n", clf)

# save model
pickle.dump(clf, open("pickle_gb_gridsearchCV.pkl", 'wb'))