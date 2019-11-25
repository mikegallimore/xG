# -*- coding: utf-8 -*-
"""
@author: micha
"""

import pandas as pd
import numpy as np

train_infile = 'training_set.csv'
train_outfile_1 = 'shots_train_MP.csv'
train_outfile_2 = 'shots_train.csv'

test_infile = 'testing_set.csv'
test_outfile_1 = 'shots_test_MP.csv'
test_outfile_2 = 'shots_test.csv'

infiles = [train_infile, test_infile]
outfiles = [train_outfile_1, train_outfile_2, test_outfile_1, test_outfile_2]

for file in infiles:
    
    ### create a dataframe from the original shots data
    shots_df = pd.read_csv(file)

    shots_df = shots_df.rename(columns={'ANGLE': 'ANGLE_MP', 'DISTANCE': 'DISTANCE_MP', 'DISTANCE_LAST_EVENT': 'DISTANCE_LAST_EVENT_MP', 'LAST_EVENT_ANGLE': 'LAST_EVENT_ANGLE_MP', 'LAST_EVENT_DISTANCE': 'LAST_EVENT_DISTANCE_MP'})

    ### change instances where the number of seconds from the last event is less than 1 to 1
    shots_df.loc[(shots_df.SECONDS_LAST_EVENT < 1), ['SECONDS_LAST_EVENT']] = 1; shots_df
   
    ### create adjusted x and y coordinates
    shots_df['X_ADJ'] = np.nan
    shots_df['Y_ADJ'] = np.nan
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.X_1 < 0), ['Y_ADJ']] = shots_df['Y_1']*-1; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.X_1 > 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.X_1 == 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.X_1 < 0), ['Y_ADJ']] = shots_df['Y_1']*-1; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.X_1 > 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.X_1 == 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 < 0), ['Y_ADJ']] = shots_df['Y_1']*-1; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 > 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 == 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Neutral') & (shots_df.X_1 < 0), ['Y_ADJ']] = shots_df['Y_1']*-1; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Neutral') & (shots_df.X_1 > 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Neutral') & (shots_df.X_1 == 0), ['Y_ADJ']] = shots_df['Y_1']; shots_df
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Defensive'),['Y_ADJ']] = shots_df['Y_1']*-1; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Defensive'),['Y_ADJ']] = shots_df['Y_1']*-1; shots_df    
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Offensive'),['X_ADJ']] = abs(shots_df['X_1']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Offensive'),['X_ADJ']] = abs(shots_df['X_1']); shots_df
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 < 0),['X_ADJ']] = 0; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 > 0),['X_ADJ']] = abs(shots_df['X_1']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 == 0),['X_ADJ']] = 0; shots_df

    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Neutral') & (shots_df.X_1 < 0),['X_ADJ']] = 0; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 > 0),['X_ADJ']] = abs(shots_df['X_1']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.HOME_ZONE == 'Neutral') & (shots_df.X_1 == 0),['X_ADJ']] = 0; shots_df

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Defensive'),['X_ADJ']] = 0; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Defensive'),['X_ADJ']] = 0; shots_df

    shots_df = shots_df[shots_df['X_ADJ'].notnull() | shots_df['Y_ADJ'].notnull()]

    shots_df['X_ABS'] = abs(shots_df['X_ADJ'])
    shots_df['Y_ABS'] = abs(shots_df['Y_ADJ'])

    ### convert the x and y coordinates to float 
    shots_df['X_1'] = shots_df['X_1'].astype(float)
    shots_df['Y_1'] = shots_df['Y_1'].astype(float)

    ### calculate the angle
    shots_df['ANGLE'] = np.nan

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Offensive'),['ANGLE']] = (shots_df['Y_ADJ'] / (np.sqrt((89 - abs(shots_df['X_1']))**2 + (shots_df['Y_ADJ']**2))) * 180) / 3.14; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Offensive'),['ANGLE']] = (shots_df['Y_ADJ'] / (np.sqrt((89 - abs(shots_df['X_1']))**2 + (shots_df['Y_ADJ']**2))) * 180) / 3.14; shots_df

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral'),['ANGLE']] = (shots_df['Y_ADJ'] / (np.sqrt((89 - abs(shots_df['X_1']))**2 + (shots_df['Y_ADJ']**2))) * 180) / 3.14; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Neutral'),['ANGLE']] = (shots_df['Y_ADJ'] / (np.sqrt((89 - abs(shots_df['X_1']))**2 + (shots_df['Y_ADJ']**2))) * 180) / 3.14; shots_df
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Defensive'),['ANGLE']] = (shots_df['Y_ADJ'] / (np.sqrt((89 + abs(shots_df['X_1']))**2 + (shots_df['Y_ADJ']**2))) * 180) / 3.14; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Defensive'),['ANGLE']] = (shots_df['Y_ADJ'] / (np.sqrt((89 + abs(shots_df['X_1']))**2 + (shots_df['Y_ADJ']**2))) * 180) / 3.14; shots_df

    shots_df.loc[(shots_df.Y_ADJ == 0),['ANGLE']] = 0; shots_df

    shots_df['ANGLE_ABS'] = abs(shots_df['ANGLE'])

    ### calculate the distance
    shots_df['DISTANCE'] = np.nan

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Offensive'),['DISTANCE']] = np.sqrt((89 - abs(shots_df['X_1']))**2 + (abs(shots_df['Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Offensive'),['DISTANCE']] = np.sqrt((89 - abs(shots_df['X_1']))**2 + (abs(shots_df['Y_1'])**2)); shots_df

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Neutral'),['DISTANCE']] = np.sqrt((89 - abs(shots_df['X_1']))**2 + (abs(shots_df['Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Neutral'),['DISTANCE']] = np.sqrt((89 - abs(shots_df['X_1']))**2 + (abs(shots_df['Y_1'])**2)); shots_df

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_ZONE == 'Defensive'),['DISTANCE']] = np.sqrt((89 + abs(shots_df['X_1']))**2 + (abs(shots_df['Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_ZONE == 'Defensive'),['DISTANCE']] = np.sqrt((89 + abs(shots_df['X_1']))**2 + (abs(shots_df['Y_1'])**2)); shots_df
          
    ### calculate the distance from the event to the last event
    shots_df['DISTANCE_LAST_EVENT'] = np.nan

    #
    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 - abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['LAST_EVENT_X_1'])) - (89 - abs(shots_df['X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df

    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 - abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['LAST_EVENT_X_1'])) - (89 - abs(shots_df['X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df

    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 - abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['LAST_EVENT_X_1'])) - (89 - abs(shots_df['X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df

    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 - abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['LAST_EVENT_X_1'])) - (89 - abs(shots_df['X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    
    #
    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 + abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df

    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 + abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 >= 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df

    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 + abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 >= 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) + abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df

    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 < 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 + abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df
    shots_df.loc[(shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 >= 0) & (shots_df.Y_1 < 0) & (shots_df.LAST_EVENT_Y_1 < 0),['DISTANCE_LAST_EVENT']] = np.sqrt(abs(((89 + abs(shots_df['X_1'])) - (89 - abs(shots_df['LAST_EVENT_X_1'])))**2) + (abs((abs(shots_df['Y_1']) - abs(shots_df['LAST_EVENT_Y_1'])))**2)); shots_df

    ### calculate the 'speed' between the event and the preceding event (see: moneypuck.com/about.htm)
    shots_df['SPEED_LAST_EVENT'] = shots_df['DISTANCE_LAST_EVENT']
    shots_df.loc[(shots_df.SECONDS_LAST_EVENT > 0), ['SPEED_LAST_EVENT']] = shots_df['DISTANCE_LAST_EVENT'] / shots_df['SECONDS_LAST_EVENT']; shots_df

    ### create, for when the event and last event were both unblocked shots, adjusted x and y coordinates for the last event
    shots_df['LAST_EVENT_X_ADJ'] = 0
    shots_df['LAST_EVENT_Y_ADJ'] = 0
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 < 0)  & (shots_df.LAST_EVENT_X_1 < 0), ['LAST_EVENT_Y_ADJ']] = shots_df['LAST_EVENT_Y_1']*-1; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0), ['LAST_EVENT_Y_ADJ']] = shots_df['LAST_EVENT_Y_1']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 < 0), ['LAST_EVENT_Y_ADJ']] = shots_df['LAST_EVENT_Y_1']*-1; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0), ['LAST_EVENT_Y_ADJ']] = shots_df['LAST_EVENT_Y_1']; shots_df
       
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block'),['LAST_EVENT_X_ADJ']] = abs(shots_df['LAST_EVENT_X_1']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block'),['LAST_EVENT_X_ADJ']] = abs(shots_df['LAST_EVENT_X_1']); shots_df
    
    shots_df = shots_df[shots_df['LAST_EVENT_X_ADJ'].notnull() | shots_df['LAST_EVENT_Y_ADJ'].notnull()]

    ### convert the x and y coordinates to float 
    shots_df['X_1'] = shots_df['X_1'].astype(float)
    shots_df['Y_1'] = shots_df['Y_1'].astype(float)

    ### calculate, for when the event and last event were both unblocked shots for the same team, the last event's angle
    shots_df['LAST_EVENT_ANGLE'] = 0

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block'),['LAST_EVENT_ANGLE']] = (shots_df['LAST_EVENT_Y_ADJ'] / (np.sqrt((89 - abs(shots_df['LAST_EVENT_X_1']))**2 + (shots_df['LAST_EVENT_Y_ADJ']**2))) * 180) / 3.14; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block'),['LAST_EVENT_ANGLE']] = (shots_df['LAST_EVENT_Y_ADJ'] / (np.sqrt((89 - abs(shots_df['LAST_EVENT_X_1']))**2 + (shots_df['LAST_EVENT_Y_ADJ']**2))) * 180) / 3.14; shots_df

    shots_df.loc[(shots_df.LAST_EVENT_Y_ADJ == 0),['LAST_EVENT_ANGLE']] = 0; shots_df

    shots_df['LAST_EVENT_ANGLE_ABS'] = abs(shots_df['LAST_EVENT_ANGLE'])

    ### calculate, for when the event and last events were both unblocked shots for the same team, the last event's distance
    shots_df['LAST_EVENT_DISTANCE'] = 0
    
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 - abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 >= 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 - abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 < 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 + abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 >= 0) & (shots_df.LAST_EVENT_X_1 < 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 + abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 < 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 - abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 < 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 - abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 >= 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 + abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.X_1 < 0) & (shots_df.LAST_EVENT_X_1 >= 0),['LAST_EVENT_DISTANCE']] = np.sqrt((89 + abs(shots_df['LAST_EVENT_X_1']))**2 + (abs(shots_df['LAST_EVENT_Y_1'])**2)); shots_df

    ### calculate, for when the event and last event were both unblocked shots for the same team, the change in angle
    shots_df['CHANGE_IN_ANGLE'] = 0

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE >= 0) & (shots_df.LAST_EVENT_ANGLE >= 0),['CHANGE_IN_ANGLE']] = abs(shots_df['ANGLE'] - shots_df['LAST_EVENT_ANGLE']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE >= 0) & (shots_df.LAST_EVENT_ANGLE < 0),['CHANGE_IN_ANGLE']] = shots_df['ANGLE'] + abs(shots_df['LAST_EVENT_ANGLE']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE < 0) & (shots_df.LAST_EVENT_ANGLE >= 0),['CHANGE_IN_ANGLE']] = abs(shots_df['ANGLE']) + shots_df['LAST_EVENT_ANGLE']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE < 0) & (shots_df.LAST_EVENT_ANGLE < 0),['CHANGE_IN_ANGLE']] = abs(abs(shots_df['ANGLE']) - abs(shots_df['LAST_EVENT_ANGLE'])); shots_df

    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE >= 0) & (shots_df.LAST_EVENT_ANGLE >= 0),['CHANGE_IN_ANGLE']] = abs(shots_df['ANGLE'] - shots_df['LAST_EVENT_ANGLE']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE >= 0) & (shots_df.LAST_EVENT_ANGLE < 0),['CHANGE_IN_ANGLE']] = shots_df['ANGLE'] + abs(shots_df['LAST_EVENT_ANGLE']); shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE < 0) & (shots_df.LAST_EVENT_ANGLE >= 0),['CHANGE_IN_ANGLE']] = abs(shots_df['ANGLE']) + shots_df['LAST_EVENT_ANGLE']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block') & (shots_df.ANGLE < 0) & (shots_df.LAST_EVENT_ANGLE < 0),['CHANGE_IN_ANGLE']] = abs(abs(shots_df['ANGLE']) - abs(shots_df['LAST_EVENT_ANGLE'])); shots_df


    ### calculate, for when the event and last event were both unblocked shots for the same team, the change of angle
    shots_df['SPEED_CHANGE_IN_ANGLE'] = 0

    shots_df.loc[(shots_df.TEAM == shots_df.HOME) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.HOME_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block'),['SPEED_CHANGE_IN_ANGLE']] = shots_df['CHANGE_IN_ANGLE'] / shots_df['SECONDS_LAST_EVENT']; shots_df
    shots_df.loc[(shots_df.TEAM == shots_df.AWAY) & (shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df.AWAY_ZONE == 'Offensive') & (shots_df.LAST_EVENT == 'Shot') & (shots_df.LAST_EVENT_TYPE != 'Block'),['SPEED_CHANGE_IN_ANGLE']] = shots_df['CHANGE_IN_ANGLE'] / shots_df['SECONDS_LAST_EVENT']; shots_df

#    shots_df.loc[(shots_df.LAST_EVENT_Y_ADJ == 0),['LAST_EVENT_ANGLE']] = 0; shots_df

    ### create dummy variables
    shots_df['IS_SHOOTER_POS_F'] = np.where(shots_df['SHOOTER_POS'].isin(['F']), 1, 0)
    
    shots_df['IS_TEAM_HOME'] = np.where((shots_df.TEAM == shots_df.HOME), 1, 0)
    
    shots_df['IS_GOAL'] = np.where(shots_df['EVENT_TYPE'].isin(['Goal']), 1, 0)
    shots_df['IS_ON_NET'] = np.where(shots_df['EVENT_TYPE'].isin(['Goal', 'Save']), 1, 0)
    
    shots_df['IS_REBOUND'] = np.where((shots_df['LAST_EVENT'] == 'Shot') & (shots_df['SECONDS_LAST_EVENT'] <= 2) & (shots_df['TEAM'] == shots_df['LAST_EVENT_TEAM']), 1, 0)
    
    shots_df['IS_BACKHAND'] = np.where(shots_df['EVENT_DETAIL'].isin(['Backhand']), 1, 0)
    shots_df['IS_REDIRECT'] = np.where(shots_df['EVENT_DETAIL'].isin(['Redirect']), 1, 0)
    shots_df['IS_SLAP'] = np.where(shots_df['EVENT_DETAIL'].isin(['Slap']), 1, 0)
    shots_df['IS_SNAP'] = np.where(shots_df['EVENT_DETAIL'].isin(['Snap']), 1, 0)
    shots_df['IS_WRAPAROUND'] = np.where(shots_df['EVENT_DETAIL'].isin(['Wraparound']), 1, 0)
    shots_df['IS_WRIST'] = np.where(shots_df['EVENT_DETAIL'].isin(['Wrist']), 1, 0)

    shots_df['IS_A_NET_EMPTY'] = np.where((shots_df.HOME_STATE == 'EN') & (shots_df.AWAY_STATE == 'EN'), 1, 0) 
    shots_df['IS_OPPOSING_NET_EMPTY'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.AWAY_STATE == 'EN') & (shots_df.AWAY_STRENGTH == '6v5') | (shots_df.TEAM == shots_df.HOME) & (shots_df.AWAY_STATE == 'EN') & (shots_df.AWAY_STRENGTH == '6v4') | (shots_df.TEAM == shots_df.HOME) & (shots_df.AWAY_STATE == 'EN') & (shots_df.AWAY_STRENGTH == '5v4') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.HOME_STATE == 'EN') & (shots_df.HOME_STRENGTH == '6v5') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STATE == 'EN') & (shots_df.AWAY_STRENGTH == '6v4') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.HOME_STATE == 'EN') & (shots_df.HOME_STRENGTH == '5v4'), 1, 0)

    shots_df['IS_TEAM_LEADING'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SITUATION == 'Leading') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SITUATION == 'LEADING'), 1, 0)
    shots_df['IS_TEAM_TIED'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SITUATION == 'Tied') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SITUATION == 'Tied'), 1, 0)
    shots_df['IS_TEAM_TRAILING'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SITUATION == 'Trailing') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SITUATION == 'Trailing'), 1, 0)

    '''    
    shots_df['IS_TEAM_UP_3_OR_MORE'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SCOREDIFF >= 3) | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SCOREDIFF >= 3), 1, 0)
    shots_df['IS_TEAM_UP_2'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SCOREDIFF == 2) | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SCOREDIFF == 2), 1, 0)
    shots_df['IS_TEAM_UP_1'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SCOREDIFF == 1) | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SCOREDIFF == 1), 1, 0)

    shots_df['IS_TEAM_TIED'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SCOREDIFF == 0) | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SCOREDIFF == 0), 1, 0)
       
    shots_df['IS_TEAM_DOWN_1'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SCOREDIFF == -1) | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SCOREDIFF == -1), 1, 0)
    shots_df['IS_TEAM_DOWN_2'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SCOREDIFF == -2) | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SCOREDIFF == -2), 1, 0)
    shots_df['IS_TEAM_DOWN_3_OR_MORE'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_SCOREDIFF <= -3) | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_SCOREDIFF <= -3), 1, 0)
    '''
    
    shots_df['IS_TEAM_EV'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STATE == 'EV') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STATE == 'EV'), 1, 0)
    shots_df['IS_TEAM_PP'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STATE == 'PP') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STATE == 'PP'), 1, 0)
    shots_df['IS_TEAM_SH'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STATE == 'SH') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STATE == 'SH'), 1, 0)
    
    '''    
    shots_df['IS_TEAM_5v5'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '5v5') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '5v5') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    shots_df['IS_TEAM_4v4'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '4v4') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '4v4') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    shots_df['IS_TEAM_3v3'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '3v3') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '3v3') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    
    shots_df['IS_TEAM_5v4'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '5v4') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '5v4') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    shots_df['IS_TEAM_5v3'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '5v3') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '5v3') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    shots_df['IS_TEAM_4v3'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '4v3') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '4v3') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    
    shots_df['IS_TEAM_4v5'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '4v5') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '4v5') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    shots_df['IS_TEAM_3v5'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '3v5') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '3v5') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    shots_df['IS_TEAM_3v4'] = np.where((shots_df.TEAM == shots_df.HOME) & (shots_df.HOME_STRENGTH == '3v4') & (shots_df.HOME_STATE != 'EN') | (shots_df.TEAM == shots_df.AWAY) & (shots_df.AWAY_STRENGTH == '3v4') & (shots_df.AWAY_STATE != 'EN'), 1, 0)
    '''
    
    shots_df['IS_LAST_EVENT_TEAM_SHOT'] = np.where((shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Shot'])), 1, 0)
    shots_df['IS_LAST_EVENT_TEAM_FACEOFF'] = np.where((shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Faceoff'])), 1, 0)
    shots_df['IS_LAST_EVENT_TEAM_TAKEAWAY'] = np.where((shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Takeaway'])), 1, 0)
    shots_df['IS_LAST_EVENT_TEAM_HIT'] = np.where((shots_df.TEAM == shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Hit'])), 1, 0)
    
    shots_df['IS_LAST_EVENT_OPP_SHOT'] = np.where((shots_df.TEAM != shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Shot'])), 1, 0)
    shots_df['IS_LAST_EVENT_OPP_FACEOFF'] = np.where((shots_df.TEAM != shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Faceoff'])), 1, 0)
    shots_df['IS_LAST_EVENT_OPP_TAKEAWAY'] = np.where((shots_df.TEAM != shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Takeaway'])), 1, 0)
    shots_df['IS_LAST_EVENT_OPP_HIT'] = np.where((shots_df.TEAM != shots_df.LAST_EVENT_TEAM) & (shots_df['LAST_EVENT'].isin(['Hit'])), 1, 0)
    
    ### filter out extremely rare event types
    shots_df = shots_df[(shots_df['HOME_STRENGTH'] != '6v3') & (shots_df['AWAY_STRENGTH'] != '6v3')]
    
    print('Finished data preparation')
    
    outfile = ''
    if file == infiles[0]:
        outfile_1 = outfiles[0]
        outfile_2 = outfiles[1]
    elif file == infiles[1]:
        outfile_1 = outfiles[2]
        outfile_2 = outfiles[3]
    
    ### write the dataframes out to a new file WITH the MoneyPuck columns
    shots_df.to_csv(outfile_1, index=False)
    print('Created ' + outfile_1)

    ### drop the MoneyPuck columns
    shots_df = shots_df.drop(columns=['LAST_EVENT_ANGLE_MP', 'LAST_EVENT_DISTANCE_MP', 'ANGLE_MP', 'DISTANCE_MP', 'DISTANCE_LAST_EVENT_MP', 'MP_XG'])
    
    ### write the dataframes out to a new file WITH the MoneyPuck columns
    shots_df.to_csv(outfile_2, index=False)
    print('Created ' + outfile_2)