# -*- coding: utf-8 -*-
"""
@author: @mikegallimore
"""

import pandas as pd
import pickle
from sklearn import metrics
from sklearn.metrics import confusion_matrix, roc_curve, auc, log_loss, roc_auc_score
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import parameters


###
### LOAD & SHAPE THE DATA
###

# set the location of the file with the seed data
shots_test_season = 'shots_test.csv'

# create a dataframe for the seed and test data; duplicate it and drop unneeded columns
test_shots_df = pd.read_csv(shots_test_season)
shots_df = test_shots_df.copy()
shots_df = shots_df.drop(columns=parameters.drop_columns)


###
### LOGISTIC REGRESSION
###

# set the independent variables for the training and test sets
continuous_variables = parameters.continuous_variables
boolean_variables = parameters.boolean_variables
independent_variables = continuous_variables + boolean_variables
x = shots_df[independent_variables]

# set the dependent variable
y = shots_df['IS_GOAL']

# load the saved model
pkl_logreg = "pickle_logreg.pkl"
with open(pkl_logreg, 'rb') as file_logreg:
    model_logreg = pickle.load(file_logreg)

# score the model
score_logreg = model_logreg.score(x, y)
print("Test score: {0:.2f} %".format(100 * score_logreg))

# score the model by accuracy
y_pred = model_logreg.predict(x)
print('Accuracy: ', metrics.accuracy_score(y, y_pred))

# generate confusion matrix
c_matrix = confusion_matrix(y_pred, y)
print(confusion_matrix(y_pred, y))
c_matrix_2 = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(c_matrix_2, annot=True)

# generate the ROC curve
fpr, tpr,_=roc_curve(y_pred, y, drop_intermediate=False)

plt.figure()

# add the ROC
plt.plot(fpr, tpr, color='red', lw=2, label='ROC curve')

# random FPR and TPR
plt.plot([0, 1], [0, 1], color='blue', lw=2, linestyle='--')

# title and labels
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC curve')
plt.show()

# score the model by ROC_AUC
auc_rating = roc_auc_score(y_pred, y)
print('AUC Score: ', auc_rating)

# score the model by log loss
print('Log Loss:\n', metrics.log_loss(y, y_pred))

# generate a classification report for the model
print('Classification Report:\n', metrics.classification_report(y, y_pred))

# generate probabilities for each shot; save probabilities to file
predictions = model_logreg.predict_proba(x)
print(predictions)

predictions_df = pd.DataFrame(predictions)

predictions_df.to_csv('test_predictions_logreg.csv', index=False)
