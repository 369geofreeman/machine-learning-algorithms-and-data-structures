#============ Logistic Regression ==========#
#==============  From Scratch  =============#
#-------------------------------------------#

import numpy as np


class LogisticRegression:

    def __init__(self, learning_rate=0.001, num_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iters = num_iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, X):
        # Returns the computed sigmoid function
        # -------------------------------------
        # X: input of 1d vector or 2d matrix
        return 1/(1+np.exp(-X))


    def fit(self, X, y):
        # Returns the traning step and gradient decent
        # --------------------------------------------------------
        # X: numpy ndarray of size m*n where m is the number of 
        #    samples and n is the number of features for each sample
        # y: A 1d row vector for size n. For each training sample
        #    We have one vector

        # Initialise parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # gradient decent
        for _ in range(self.n_iters):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self._sigmoid(linear_model)
            der_weight = (1 / n_samples) * np.dot(X.T, y_predicted - y)
            der_bias = (1 / n_samples) * np.sum(y_predicted - y)
            self.weights -= self.learning_rate * der_weight
            self.bias -= self.learning_rate * der_bias


    def predict(self, X):
        # Returns the predicted classes as 0 or 1
        # ---------------------------------------
        # X: numpy ndarray of size m*n

        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self._sigmoid(linear_model)
        y_predicted_classes = [1 if i > 0.5 else 0 for i in y_predicted]

        return y_predicted_classes


