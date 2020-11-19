# A file to generate a visulisation of a number of activation function
# using matplotlib

import numpy as np
import matplotlib.pyplot as plt


def plot(func, yaxis=(-1.4, 1.4)):
    plt.ylim(yaxis)
    plt.locator_params(nbins=5)
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.axhline(lw=1, c='black')
    plt.axvline(lw=1, c='black')
    plt.grid(alpha=0.4, ls='-.')
    plt.plot(x, func(x), c='r', lw=3)


x = np.arange(-5, 5, 0.01)

# ========= Binary Step ========= #


def binary_step(x):
    return np.vectorize(lambda x: 1 if x > 0 else 0, otypes=[np.float])


# plot(binary_step(x), yaxis=(-0.4, 1.4))
# plt.show()


# ======== Linear Function ========= #

def linear_function():
    plt.xticks(fontsize = 14)
    plt.yticks(fontsize = 14)
    plt.axhline(lw=1, c='black')
    plt.axvline(lw=1, c='black')
    plt.grid(alpha=0.4, ls='-.')
    plt.plot([-2, 2], [-2, 2], c='r', lw=3)
    plt.show()

# linear_function()


# ======== Sigmoid Function ========= #


def sigmoid_function(x):
    z = (1/(1 + np.exp(-x)))
    return z


plot(sigmoid_function, yaxis=(-0.4, 1.4))

plt.show()














