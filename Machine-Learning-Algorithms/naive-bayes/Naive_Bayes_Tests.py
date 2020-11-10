# ------------------------------------------------- #
# ============= Test Naive Bayes  ================= #
# ------------------------------------------------- #

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets

from Naive_Bayes import NaiveBayes


def accuracy(y_true, y_pred):
    # Returns the accuracy of a model
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


# select and split the data
X, y = datasets.make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=123)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# initiate and train our model
nb = NaiveBayes()
nb.fit(X_train, y_train)

# Predict
predictions = nb.predict(X_test)


# Print results
print("Naive Bayes classification accuracy:", accuracy(y_test, predictions))




