# ------------------------------------------------- #
# ============ Digit Classification  ============== #
# ------------------------------------------------- #


from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import numpy as np
from matplotlib import pyplot


digits = load_digits()

ss = StandardScaler(with_std=False)
X = ss.fit_transform(digits['data'])

Knn = NearestNeighbors(algorithm="ball_tree", n_neighbors=25, leaf_size=30)
Knn.fit(X)

x_noise = X[50] = np.random.normal(0.0, 1.5, size=(64, ))

distances, neighbors = Knn.kneighbors(x_noise.reshape(1, -1), return_distance=True)


# Print the distances
print(distances[0])

# Print the results

for i in range(25):
    pyplot.subplot(330 + 1 + i)
    pyplot.imshow(digits.images[distances[0][i]], cmap=pyplot.get_cmap('gray'))
pyplot.show()



