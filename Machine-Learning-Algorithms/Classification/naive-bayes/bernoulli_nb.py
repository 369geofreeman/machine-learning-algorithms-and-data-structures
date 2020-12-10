from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split

nb_samples = 300

X, y = make_classification(n_samples=nb_samples, n_features=2, n_informative=2, n_redundant=0)


plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=25, edgecolor='k')
plt.show()



X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25)

bnb = BernoulliNB(binarize=0.0)
bnb.fit(X_train, y_train)

score = bnb.score(X_test, y_test)

print('The score for Bernoulli Naive Bayes is:', score)


