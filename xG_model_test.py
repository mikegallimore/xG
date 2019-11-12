# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""
###
### IMPORT NEEDED PACKAGES
###

import pandas as pd
import pickle
from sklearn import metrics
from sklearn.metrics import confusion_matrix, roc_curve, auc, log_loss, roc_auc_score
import seaborn as sn
import matplotlib.pyplot as plt

###
### LOAD & SHAPE THE DATA
###

### set the location of the file with the seed data
shots_test_season = 'shots_test.csv'

### create a dataframe for the seed and test data; duplicate it and drop unneeded columns
test_shots_df = pd.read_csv(shots_test_season)
shots_df = test_shots_df.copy()
shots_df = shots_df.drop(columns=['SEASON', 'GAME_ID', 'HOME', 'AWAY', 'HOME_GOALS', 'AWAY_GOALS', 'HOME_SCOREDIFF', 'AWAY_SCOREDIFF', 'HOME_SITUATION', 'AWAY_SITUATION', 'HOME_ZONE', 'AWAY_ZONE', 'X_1', 'Y_1', 'ANGLE', 'LAST_EVENT_TYPE', 'MP_XG'])

###
### CREATE THE LOGISTIC REGRESSION
###

### set the independent variables for the training (5 seasons) and test (1 season) sets
continuous_variables = ['SECONDS_LAST_EVENT', 'X_ADJ', 'Y_ADJ', 'ANGLE_ADJ', 'DISTANCE', 'DISTANCE_LAST_EVENT']
boolean_variables = ['IS_SHOOTER_POS_F', 'IS_TEAM_HOME', 'IS_ON_NET', 'IS_REBOUND', 'IS_A_NET_EMPTY', 'IS_TEAM_UP_3_OR_MORE', 'IS_TEAM_UP_2', 'IS_TEAM_UP_1', 'IS_TEAM_TIED', 'IS_TEAM_DOWN_1', 'IS_TEAM_DOWN_2', 'IS_TEAM_DOWN_3_OR_MORE', 'IS_TEAM_5v5', 'IS_TEAM_4v4', 'IS_TEAM_3v3', 'IS_TEAM_5v4', 'IS_TEAM_5v3', 'IS_TEAM_4v3', 'IS_TEAM_4v5', 'IS_TEAM_3v5', 'IS_TEAM_3v4']
independent_variables = continuous_variables + boolean_variables
x = shots_df[independent_variables]

### set the dependent variable
y = shots_df['IS_GOAL']

pkl_logreg = "pickle_gb_gridsearchCV.pkl"
with open(pkl_logreg, 'rb') as file_logreg:
    model_logreg = pickle.load(file_logreg)

score_logreg = model_logreg.score(x, y)
print("Test score: {0:.2f} %".format(100 * score_logreg))

y_pred = model_logreg.predict(x)
print('Accuracy: ', metrics.accuracy_score(y, y_pred))

c_matrix = confusion_matrix(y_pred, y)
print(confusion_matrix(y_pred, y))
c_matrix_2 = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(c_matrix_2, annot=True)

### generate the ROC curve
fpr, tpr,_=roc_curve(y_pred, y, drop_intermediate=False)

plt.figure()
##Adding the ROC
plt.plot(fpr, tpr, color='red',
 lw=2, label='ROC curve')
##Random FPR and TPR
plt.plot([0, 1], [0, 1], color='blue', lw=2, linestyle='--')
##Title and label
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC curve')
plt.show()

### generate the AUC score
auc_rating = roc_auc_score(y_pred, y)
print('AUC Score: ', auc_rating)

print('Log Loss:\n', metrics.log_loss(y, y_pred))

print('Classification Report:\n', metrics.classification_report(y, y_pred))

predictions = model_logreg.predict_proba(x)[0:100]
print(predictions)