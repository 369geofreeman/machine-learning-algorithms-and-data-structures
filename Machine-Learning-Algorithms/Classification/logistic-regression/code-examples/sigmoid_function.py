#==================== Sigmoid Function ==================#

# A function maps any real value into another value between 0 and 1. In machine learning, we us sigmoid to map predictions to probabilities.


# First we can plot what the Sigmoid function looks like 

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 10, 100)
y = 1/(1 + np.exp(-x))

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")

plt.show()



# And now we run our implementation of the sigmoid function

def sigmoid(z):
    """
    Compute sigmoid function given the input z.

    Parameters
    ----------
    z : array_like
        The input to the sigmoid function. This can be a 1-D vector
        or a 2-D matrix.

    Returns
    -------
    g : array_like
        The computed sigmoid function. g has the same shape as z, since
        the sigmoid is computed element-wise on z.

    Instructions
    ------------
    Compute the sigmoid of each value of z (z can be a matrix, vector or scalar).
    """
    # convert input to a numpy array
    z = np.array(z)

    # We need to return the following variables correctly
    g = np.zeros(z.shape)

    # Compute the sigmoid for each value of z
    g = (1/(1+np.exp(-z)))

    return g





# Test the implementation of sigmoid function here
z = 0
g = sigmoid(z)

print('g(', z, ') = ', g)
# -> returns 0.5

# Plot the results
x = np.arange(-10., 10., 0.2)
z = sigmoid(x)

plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")

plt.show()

