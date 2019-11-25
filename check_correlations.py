# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

import pandas as pd
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
### CHECK THE CORRELATIONS
###

corr = shots_df.corr()['IS_GOAL'][shots_df.corr()['IS_GOAL'] < 1].abs()
corr = corr.sort_values(ascending=False)
print(corr)
