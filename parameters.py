# -*- coding: utf-8 -*-
"""
@author: micha
"""
### trim the dataframe
drop_columns = ['SEASON', 'PERIOD', 'GAME_ID', 'HOME', 'AWAY', 'HOME_GOALS', 'AWAY_GOALS', 'HOME_SCOREDIFF', 'AWAY_SCOREDIFF', 'HOME_SITUATION', 'AWAY_SITUATION', 'HOME_ZONE', 'AWAY_ZONE', 'X_1', 'Y_1', 'X_ADJ', 'Y_ADJ', 'SHOOTER_NO', 'LAST_EVENT_X_1', 'LAST_EVENT_Y_1', 'LAST_EVENT_X_ADJ', 'LAST_EVENT_Y_ADJ', 'ANGLE', 'LAST_EVENT_ANGLE', 'LAST_EVENT_ANGLE_ABS', 'LAST_EVENT_DISTANCE', 'CHANGE_IN_ANGLE', 'IS_TEAM_HOME', 'IS_A_NET_EMPTY']

### select the features
continuous_variables = ['SECONDS_GONE', 'SECONDS_LAST_EVENT', 'X_ABS', 'Y_ABS', 'ANGLE_ABS', 'DISTANCE', 'DISTANCE_LAST_EVENT', 'SPEED_LAST_EVENT', 'SPEED_CHANGE_IN_ANGLE']
boolean_variables = ['IS_SHOOTER_POS_F', 'IS_ON_NET', 'IS_REBOUND', 'IS_LAST_EVENT_TEAM_SHOT', 'IS_LAST_EVENT_TEAM_FACEOFF', 'IS_OPPOSING_NET_EMPTY', 'IS_TEAM_LEADING', 'IS_TEAM_TIED', 'IS_TEAM_TRAILING', 'IS_TEAM_EV', 'IS_TEAM_PP', 'IS_TEAM_SH']