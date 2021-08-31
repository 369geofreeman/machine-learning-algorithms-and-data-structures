'''
Using the Bayesian theorem to solve probability of the farmer and the librarian

Abstract
---
From Daniel Kahneman's  book, Thinking, Fast and Slow:

An individual has been described by a neighbor as follows: “Steve is very shy and
withdrawn, invariably helpful but with very little interest in people or in the
world of reality. A meek and tidy soul, he has a need for order and structure,
and a passion for detail.” Is Steve more likely to be a librarian or a farmer?

'''

from IPython.core.pylabtools import figsize
from matplotlib import pyplot as plt


figsize(12.5, 4)
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300

colors = ['#348ABD', '#A60628']
prior = [1/21., 20/21.]
posterior = [0.087, 1-0.087]

plt.bar([0, .7], prior, alpha=0.70, width=0.25,
       color=colors[0], label="prior distribution",
       lw="3", edgecolor="#348ABD")

plt.bar([0+0.25, .7+0.25], posterior, alpha=0.7, width=0.25,
       color=colors[1], label="Posterior distribution",
       lw="3", edgecolor="#A60628")

plt.xticks([0.20, 0.95], ["Librarian", "Farmer"])
plt.title("Prior and prosterior probabilities of Steve's\
           occupation")
plt.ylabel("Probability")
plt.legend(loc="upper left")

plt.show()
