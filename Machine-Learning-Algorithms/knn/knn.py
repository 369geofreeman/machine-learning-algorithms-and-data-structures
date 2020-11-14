# ----------------------------------------------- #
# ============ K Nearest Neighbors ============== #
# ----------------------------------------------- #


import numpy as np
from collections import Counter


def eucledean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


class KNN:

    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        """
        Will fit the training samples
        X: Traning samples - numpy md array, m*n size
        y: Traning labels - 1d row vector
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """
        return multiple samples
        """
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        """
        Helper method to return one sample
        Computes the distances
        get k nearest samples, labels
        get majority vote, most common class label
        """
        distances = [eucledean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)

        return most_common[0][0]




