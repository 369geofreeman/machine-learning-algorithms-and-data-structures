# ------------------------------------------------------- #
# ============ TESTING K NEAREST NEIGHBOR  ============== #
# ------------------------------------------------------- #


import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# load and seperate the data

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)


# print and plot the data so we can visualise it

print('The training data is of size {}, an example of it is: {}'
      .format(X_train.shape, X_train[0]))
print('The labels are size {}, an example is: {}'
      .format(y_train.shape, y_train[4]))


plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolor='k', s=20)
plt.show()


# Test with our model

from knn import KNN

clf = KNN(k=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

acc = np.sum(predictions == y_test) / len(y_test)

print('Accuracy of KNN model: {}%'.format(acc * 100))


