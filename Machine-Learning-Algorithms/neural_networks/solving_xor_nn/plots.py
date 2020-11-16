# Code to produce graphs used in README.md

import matplotlib.pyplot as plt
import numpy as np


# Linearly seprable

x1 = np.random.randint(1, 6, size=5)
y1 = np.random.randint(1, 6, size=5)

x2 = np.random.randint(5, 11, size=5)
y2 = np.random.randint(5, 11, size=5)

plt.scatter(x1, y1, c='r', s=200, marker="^")
plt.scatter(x2, y2, c='g', s=200, marker="P")
plt.plot([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Linearly seprable')
plt.grid(True)
plt.show()


# XOR - Not linearly seperable

x3 = np.array([[0, 0], [1, 1]])
x4 = np.array([[0, 1], [1, 0]])


plt.scatter([0, 1], [0, 1], c='r', s=200, marker="^")
plt.scatter([0, 1], [1, 0], c='g', s=200, marker="P")

plt.title('Not linearly seprable')
plt.grid(True)
plt.show()






