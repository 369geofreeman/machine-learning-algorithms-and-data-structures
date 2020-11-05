# ------------------------------------------------------ #
# ============= Test Logistic Regression =============== #
# ------------------------------------------------------ #


# - A script to test an implementation of logistic regression

# - Data set from sklearn - Breast cancer dataset to determin whether a
#   tumor is malignant or benign.

# - We split the data into traning and test samples. We then create a logistic
#   Regression model from the class we implemented and fit the traning data
#   and traning labels. Finally we use this to predict the labels for the
#   test data.

# - We also calculate the accuracy, how many of the labels are correctly
#   classified


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib as plt

from logistic_regression import LogisticRegression

bc_data = datasets.load_breast_cancer()
X, y = bc_data.data, bc_data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


regressor = LogisticRegression(learning_rate=0.001, num_iterations=1000)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)


print("Logistic Regression classification accuracy:", accuracy(y_test, predictions))







