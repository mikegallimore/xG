# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:42:14 2019

@author: Michael
"""
###
### IMPORT NEEDED PACKAGES
###

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix, roc_curve, auc, log_loss, roc_auc_score

###
### LOAD & SHAPE THE DATA
###

### set the location of the file with the seed data
shots_training_seasons = 'shots_training-seasons.csv'

### create a dataframe of the seed data; duplicate it and drop unneeded columns
shots_df = pd.read_csv(shots_training_seasons)
xg_df = shots_df.copy()
xg_df = xg_df.drop(columns=['HOME_ZONE', 'AWAY_ZONE', 'XG_MONEYPUCK'])


###
### CREATE THE LOGISTIC REGRESSION
###

### set the independent variables
continuous_variables = ['SECONDS_GONE','SECONDS_LAST_EVENT','X_1', 'Y_1', 'ANGLE', 'DISTANCE', 'DISTANCE_LAST_EVENT']
boolean_variables = ['IS_ON_NET', 'IS_REBOUND', 'IS_HOME_LEADING', 'IS_HOME_TIED', 'IS_HOME_TRAILING', 'IS_HOME_EV', 'IS_HOME_PP', 'IS_HOME_SH']
independent_variables = continuous_variables + boolean_variables
x = xg_df[independent_variables]

### set the dependent variable
y = xg_df['IS_GOAL']

### apply train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

### apply the logistic regression
logistic_regression = LogisticRegression()
logistic_regression.fit(x_train,y_train)
y_pred=logistic_regression.predict(x_test)


###
### EVALUATION
###

### create a confusion matrix#
#c_matrix = confusion_matrix(y_pred, y_test)
#print(confusion_matrix(y_pred,y_test))
c_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(c_matrix, annot=True)

### get the accuracy
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))

### generate the ROC curve
fpr, tpr,_=roc_curve(y_pred,y_test,drop_intermediate=False)

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
auc_rating = roc_auc_score(y_pred,y_test)
print('AUC Score: ',auc_rating)
