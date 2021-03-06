# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

# trim the dataframe
drop_columns = ['SEASON', 'PERIOD', 'GAME_ID', 'HOME', 'AWAY', 'HOME_GOALS', 'AWAY_GOALS', 'HOME_SCOREDIFF', 'AWAY_SCOREDIFF', 'HOME_SITUATION', 'AWAY_SITUATION', 'HOME_ZONE', 'AWAY_ZONE', 'SECONDS_LAST_EVENT', 'X_1', 'Y_1', 'X_ADJ', 'Y_ADJ', 'SHOOTER_NO', 'LAST_EVENT_X_1', 'LAST_EVENT_Y_1', 'LAST_EVENT_X_ADJ', 'LAST_EVENT_Y_ADJ', 'ANGLE', 'LAST_EVENT_ANGLE', 'LAST_EVENT_ANGLE_ABS', 'LAST_EVENT_DISTANCE', 'CHANGE_IN_ANGLE', 'IS_ON_NET', 'IS_TEAM_HOME']

# select the features
continuous_variables = ['SECONDS_GONE', 'X_ABS', 'Y_ABS', 'ANGLE_ABS', 'DISTANCE', 'DISTANCE_LAST_EVENT', 'SPEED_LAST_EVENT', 'SPEED_CHANGE_IN_ANGLE']
boolean_variables = ['IS_SHOOTER_POS_F', 'IS_REBOUND', 'IS_LAST_EVENT_TEAM_SHOT', 'IS_LAST_EVENT_OPP_SHOT', 'IS_LAST_EVENT_TEAM_FACEOFF', 'IS_LAST_EVENT_OPP_FACEOFF', 'IS_LAST_EVENT_TEAM_GIVEAWAY', 'IS_LAST_EVENT_OPP_GIVEAWAY', 'IS_LAST_EVENT_TEAM_TAKEAWAY', 'IS_LAST_EVENT_OPP_TAKEAWAY', 'IS_LAST_EVENT_OPP_HIT', 'IS_LAST_EVENT_TEAM_HIT', 'IS_TEAM_NET_EMPTY', 'IS_OPP_NET_EMPTY', 'IS_TEAM_UP_3_OR_MORE', 'IS_TEAM_UP_2', 'IS_TEAM_UP_1', 'IS_TEAM_TIED', 'IS_TEAM_DOWN_1', 'IS_TEAM_DOWN_2', 'IS_TEAM_DOWN_3_OR_MORE', 'IS_TEAM_5v5', 'IS_TEAM_4v4', 'IS_TEAM_3v3', 'IS_TEAM_5v4', 'IS_TEAM_5v3', 'IS_TEAM_4v3', 'IS_TEAM_4v5', 'IS_TEAM_3v5', 'IS_TEAM_3v4']
