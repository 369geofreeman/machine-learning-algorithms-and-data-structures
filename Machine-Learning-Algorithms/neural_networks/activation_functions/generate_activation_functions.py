# A file to generate a visulisation of a number of activation function
# using matplotlib

# Uncomment plt of required function to see graph

# Hard Limit / Binary Step
# Linear Function
# Sigmoid Function
# Tanh Function
# ArcTan Function
# ReLU Function
# Leaky ReLU
# Exponential Linear Units, ELU
# Swish

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


# plot(sigmoid_function, yaxis=(-0.4, 1.4))

# plt.show()


# ========= Tanh Function ========= #

def tanh_function(x):
    z = (2/(1 + np.exp(-2*x))) -1
    return z

# plot(tanh_function)
# plt.show()



# ========= Arctan Function ======== #


def arctan(x):
    return np.arctan(x)


# plot(arctan)
# plt.show()


# ======== ReLU Function ======== #

def relu_function(x):
    return np.vectorize(lambda x: 0 if x < 0 else x, otypes=[np.float])


# plot(relu_function(x), yaxis=(-0.4, 4))
# plt.show()


# ========= Leaky ReLU Function ======== #

def leaky_relu_function(x):
	return np.vectorize(lambda x: max(0.05 * x, x), otypes=[np.float])


# plot(leaky_relu_function(x), yaxis=(-0.4, 4))
# plt.show()


# ======== Exponential Linear Units, ELU ======== #


def elu_function(x):
    return np.vectorize(lambda x: x if x > 0 else 0.5 * (np.exp(x) - 1), otypes=[np.float])

# plot(elu_function(x))
# plt.show()



# ========== Swish ========= #


x = np.arange(-5, 5, 0.01)
y = []
beta = 0.9
for i in x:
    y.append(i*sigmoid_function(beta*i))

plt.plot(x, y, c='r', lw=3)
plt.show()

















