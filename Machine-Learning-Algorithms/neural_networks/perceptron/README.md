# Perceptron



### Code

* The full code can be [found here](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/blob/main/Machine-Learning-Algorithms/neural_networks/perceptron/perceptron.py)
* A script to test the perceptron can be found [here](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/blob/main/Machine-Learning-Algorithms/neural_networks/perceptron/perceptron_tests.py)


### Contents

  * [A Brief History](#a-brief-history)
  * [Overview](#overview)
  * [Simple Pattern Recognition](#simple-pattern-recognition)
  * [Perceptron learning Rule](#perceptron-learning-rule)
  * [Perceptron from Scratch](#perceptron-from-scratch)


## A Brief History

_**"If the brain was simple enough to be understood - we would be too simple to understand it!"**_ - Marvin Minsky

Developed in 1958 at the  Cornell Aeronautical Laboratory by Frank Rosenblatt, the Perceptron algorithm is based on a simplified model of a biological neuron and is considered to be the first working example of a thinking machine.

To understand how this concept came to be, we can look at the background leading up to the creation of the Perceptron starting with the neuron.

A neuron is an electrically excitable cell that communicates with other cells via specialized connections called synapses

<img src="img/img0.png" alt=" " width="600"/>

Here we can see a neuron is made up of Dendrite, soma and axon. Signals come through the dendrites into the soma and then goes out via the axon to other neurons

Mathematically we can view a neuron like this

<img src="img/img11.png" alt=" " width="600"/>

The above image is from the 1943 paper _"A logical calculus of the ideas immanent in nervous activity"_ [found here](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) written by WARREN S. MCCULLOCH AND WALTER PITTS

This could easily be viwed as the first real origin in the development of _thinking machines_ by modern standards. it shows us that a neuron has two incoming synaptic connections. The first, called the excitatory synapse (shown in green), transmits weighted input to the neuron. If the total number of of synaptic connections (input) exceeds the threshold, the neuron will fire.
That is unless the second connection sends a signal. If the inhibitory synapse (second signal) does send any signal it will prevent the neuron from firing.

This is a very powerful  idea and it means that using this model we can produce lots of boolean functions.
For instance, we can show this with boolean gates.

For the following examples we will set the threshold to 2. Ie, in order to send an output pulse, each neuron must receive two excitory inputs and no inhibitory inputs.

_Lines ending in a dot represent exatory connections, lines ending in a hoop represent inhibitory connections._

<img src="img/img22.png" alt=" " width="300"/>


Here we have a signal coming in from 1 (the first neuron) that connects to the second neuron (2) with two synapses. The incoming signal is 2 which meets our threshold requirements so the second neuron is fired afterwards. This is a **delay**


<img src="img/img33.png" alt=" " width="300"/>


Now in this example we have 2 neurons (1 and 2) each connecting to neuron 3 with two synapses, if either of the two signals fire it will cause nauron 3 to fire because we again meet the threshold. This is an **OR boolean gate.**

Now following the same logic, we can recognise the following two boolean gates as:

<img src="img/img4.png" alt=" " width="300"/>

**AND logic gate**

<img src="img/img5.png" alt=" " width="300"/>

**1 and NOT 2 logic gate (2 cannot fire but 1 must fire)**


So using these basic units, we can construct fairly complecated boolean circuits but can this machine think or learn?
Well no. Despite this and  proposed theories, no learning mechanism was ever produced by McCulloch and Pitts, but it was a good starting point.


A few years later in 1958,  Frank Rosenblatt came up with the algorithm for the Perceptron that was a step further than what had been created before. 

here we can see a simplified mathmatical model of it


<img src="img/img6.png" alt=" " width="700"/>


As we can see, it more closely relates to that of a neuron cell. What makes the pecptron superiour to MacCulloch and Pitts model is the use of weights associated with the inputs.
Basically, this means that the total input that the neuron gets is that of the weighted sum of all of the the inputs. Each input is multiplied by it's weight and all of them combined will equal the weighted sum that the neuron recieves. 

if this weighted sum exceeds a predetermined threshold, then the neuron will fire.

Mathmatically we can write this as:

<img src="img/img7.png" alt=" " width="600"/>

Upon the conception of the Perceptron, Roosenblatt assumed it could represent any boolean circuit and perform any computation. This led to extremely large funding from the US Navy and once the media got wind of it, extreme exageration:

**_"The embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence."_** - The New York Times - 1958


**_"Frankenstien monsterdesigned by Navy that thinks"_** - Tulsa, Oklahoma Times - 1958

As well as coming up with the model, Roosenblatt also provided a learning mechanism.
He realised that if he wanted this unit to learn a specific function he could keep providing it examples of input/output pairs. If he recieved a wrong (boolean) output, he could simply adjust the weights by the difference of what the output must be and what the output really is. (We will dive further into this later). This is known as the **Perceptron learnig rule**

The proved mathmatically that this converged and if the result could be represented as a boolean, it would converge to the correct solution.

[This video](https://www.youtube.com/watch?v=7BtLqqJVP9w&ab_channel=ComputerweltPodcast) shows him using it to predict the gender of a person by looking at a photograph.

The Perceptron could also solve the same logic gates as McCulloch & Pitts model but this hype wasnt to last long.
There was one logic gate that it couldn't solve, the XOR gate. A book published by Marvin Minsky and Seymour Papert in 1969 called _"perceptrons"_ showed solving an XOR gate with a single layer Perceptron to be impossible.

This ultimatly contributed towards what is known as the AI winter, where funding dried up and slowed research when the promises of AI was not realised.

It's important to note that despite the claims of a multi-layer Perceptron still not being able to solve the XOR problem (again from Minsky and Paperts book) where not true. We explore this idea and prove it using a neural netwrok here: [Solving XOR with a Neural Network](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/tree/main/Machine-Learning-Algorithms/neural_networks/solving_xor_nn)


## Overview

The single layer, or single neuron  percptron is a FeedForward neural network. Ie, a neural networks where the connections between units do not form a cycle.
Single neuron perceptrons can calssify input vectors into a binary output, because of this, in general a hard limit / binary-step activation function is used.
The hard limit activation function sets the output of the neuron to 0 if the function argument is less than 0, or 1 if the argument is greater than or equal to 0.

The formula can be written as:
```
	       { 1 if x ≧ 0
	f(x) = |
     	       { 0 if x < 0
```
 And it can be visualised like so:


<img src="img/img1.png" alt=" " width="600"/>


Using this, if we have a two input perceptron it could be written like so:
```
	W₁,₁ = -1
	W₁,₂ = 1

then
	a = hardlim(n)
	a = hardLim(wp+b)
	a = hardlim([-1, 1]p + b)

``` 
It's important to understand that the W represents the **weight matrix** which can be viwed like so:
```
	    _ 		     _
	    |W₁,₁ W₁,₂ ⋯ W₁,ᵣ|
	W = |W₂,₁ W₂,₂ ⋯ W₂,ᵣ|
	    |  ⋮    ⋮      ⋮ |
	    |W𝙨,₁ W𝙨,₂ ⋯ W𝙨,ᵣ|
	    -		     -
```
A weighted matrix follows two rules:
* The number of rows must equal the number of neurons in the previous layer
* The number of columns must match the number of neurons in the next layer

And b is the **bias**. A bias term allows us to shift neurons activation outputs left and right. This helps us model datasets that do not necessarily pass through the origin.


So given this, if the inner product of the weight matrix with the input vector is greater than or equal to -b, it will be -1. 
This divides the input space into two parts. if b is is equal to -1 we can visualise it like so 

<img src="img/img2.png" alt=" " width="600"/>

The posiition of the boundry is shifted by changing the value of the bias **(b)**. The line seperating the input space is called the decision boundry which can be seen as the blue line above seperating the shaded region and clear region of the input space.
The shaded region containes all the input vectors for which the output will be 1 and the non-shaded region will be -1 for all other input vectors.
It's important to note that the decision boundry will always be orthogonal to the weight matrix **(W)**

The decision boundry between the two seperated categories can be written as the following equation:
```
	Wp+b = 0
```

Ultimatly the key property of the single-neuron perceptron is that it can seperate input vectors into two categories.

The downside to this is of course it can ony be used to recognise patterns that are linearly seperable.





## Simple Pattern Recognition


To illustrate this further we can use the classic example of using a single layer perceptron to recognise if the object given is an apple or an orange based off of 3 features that output a +1 or -1 dependant of the outcome.

The features we will be using are:
* Weight
* Shape - round or elliptical
* Texture - smooth or rough 

For instance, if the fruit weighs more than a predetermined amount it will output 1, less than that and it will be -1.

For the remainder of this example we will use 2 prototype feature vectors for an apple and an orange like so:
```
if
	    | shape |
	p = |texture|
	    |weight |

then our apple will be:

	    | 1 |
	p = |-1 |
	    |-1 |

And our orange will be:

	    | 1 |
	p = | 1 |
	    |-1 | 
```


This means our vector inputs are three dimensional (r=3), so our perceptron equation will be:
```
		    |		     |p₁|     |
	a = hardlims|[W₁,₁ W₁,₂ W₁,₃]|p₂| + b |
		    |		     |p₃|     |
```

Choosing the bias is easy because we want the output to be either a -1 if it's an orange, or +1 if it's an apple.

Next we will need a linear boundry that can seperate our oranges and apples

Using our prototype apple and orange vectors we defined above, we can set our linear boundry to symetrically divide them with the p₁, p₃ plane shown below


<img src="img/img3.png" alt=" " width="600"/>

Since the p₁, p₃ plane is our decision boundry, we can write the equation for it as:
```
	p₂ = 0

or
	       |p₁|
	[0 1 0]|p₂| + 0 = 0
	       |p₃|

```
Therefore the weight matrix and bias will be

* w = [0 1 0]
* b = 0 

The bias is 0 because we pass through the origin. 
W, the weight matrix is orthoginal to the decision boundry and therefore points towards the region that contains the prototype pattern p₂ (apple)

Now we have this set up we can test this by passing some examples. First we can use our prototype examples:

**Orange**
```
  	 	            | 1 |    
	a = hardlim( [0 1 0]|-1 | + 0) = -1 (orange)
		            |-1 |    
```

**Apple**
```
		            | 1 |
	a = hardlim( [0 1 0]| 1 | + 0) = +1 (apple)
			    |-1 | 
```


This seems to be wroking well. But what if we pass in some not-so-perfect fruits?

Lets pass in a misshaped orange where
```
	    |-1|
	p = |-1|
	    |-1|
```

The response of our perceptron would be:
```
			   |-1|
	a = hardlim([0 1 0]|-1| + 0) = -1(orange)
			   |-1|
```

Again a success. We can in fact, input any vectors that are closer to the perfect orange prototype (using Euclidean distance) and it will recognise it as such. The same goes for apples as well.


## Perceptron learning Rule

No we can look at the algorithm for tranning perceptron networks.

the learning rule can be described by a procedure for modling the weights and biases fo a network, sometimes also called "the training algorithm", We are essentually using the learning rule to train the network to perform some task.

As we discussed earlier, the output of the network is given by
```
	a = hardlim(Wp+b)
```
where hardlim is the activation function

More about activation functions [can be found here](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/tree/main/Machine-Learning-Algorithms/neural_networks/activation_functions)


So given this, if the inner product of the ith row of the weight matrix where the input vector is greater or equal to -b, the output will be 1, else the output will be 0.

Let's test this with a simple two-input Perceptron.

The output will be determined by 'a', our activation function. we can write a like so
```
	a = hardlim(n)
	a = hardlim(Wp+b)
	a = hardlim(₁wᵀp+b)
	a = hardlim(w₁,p₁+w₁,2p₂+b)
```

The decision boundry is determined by the input vectors for which the net input n is zero.
```
	n = ₁wᵀp+b
	  = w₁,₁p₁+w₁,₂p₂+b
	  = 0
```

To better understand this, we can assign values for the weights and biases

* w₁,₁ = 1
* w₁,₂ = 1
* b =   -1

This would then make our decision boundry as follows:
```
	n = ₁wᵀp+b
 	  = w₁,₁p₁+w,₂p₂+b
	  = p₁+p₂ -1
	  = 0
```


This gives us our decision boundry, a line where one side of the plane will be 1, and the other will be 0.

To draw the line we need to find the points where it intersects the p₁ and p₂ axes.

To find the p₂ intercept, set p₁ = 0:
```
	        b      -1
	p₂ = - ---- = ---- = 1 if p₁ = 0
	       w₁,₂    1
```


similary, to find the p₁ intercept, set p₂ = 0
```
	        b      -1
	p₁ = - ---- = ---- = 1 if p₂ = 0
	       w₁,₁    1
```


As seen below, this creates the following decision boundry


<img src="img/img12.png" alt=" " width="600"/>

To find out which side of the boundry is equal to 1, we can test just one point. For input [2 0]ᵀ, the network output will be 
```
	a = hardlim(₁wᵀp+b) = hardlim([1 1]|2| -1) = 1
					   |0|
```

This is shown in the above image as the shaded area. Also, remember the boundry si always orthogonal to ₁w.

The Perceptron learning rule is a great example of supervised training. We will use a test problem to illustrate this.

The input/target pairs for our test problem are:

<img src="img/img13.png" alt=" " width="600"/>


We can view this on a graph like so, where the shaded circle is a 1 and the empty circle is a 0


<img src="img/img14.png" alt=" " width="600"/>


This network will have 2 inputs and a single output. For simplicity we not use a bias for this so the decision boundry will pass through the origin.

To begon traning we will asssign some initial values for the network parameters. In our case, because we are only training a two-input/single-output network without a bias, we only have to initialise it's two weights. To start with, we initilise these weights randomly.
```
	₁wᵀ = [1.0 -0.8]
```

Now we can present the input vectors to the network. let's begin with p₁
```
	a = hardlim(₁wᵀp₁)
	  = hardlim([1.0 -0.8]|1|)
			      |2|
	  = hardlim(-0.6) = 0
```

The result is 0. As we can see the network has not returned the correct value. we expected the result, t₁, to equal 1.
So what we need to do is alter the weight vector so that it points more towards p₁, that should insure a better chance of classifying it correctly.

One possible way is to set up some rules. For instance in this case we can add p₁ to ₁w.
Adding p₁ to ₁w would make ₁w point more in the direction of p₁. Repeated presentations of p₁ would cause the direction of ₁w to asymptotically approach the direction of p₁

This rule can be stated as:
```
	if t=1 and a=0, then ₁w(new) = ₁w(old) + p
```

Applying this rule to our test problem results in new values for ₁w
```
	₁w(new) = ₁w(old) +p₁
		= | 1.0| + |1| = |2.0|
		  |-0.8|   |2|   |1.2|
```

We now move on to the next input vector and continue making changes to the weights and cycling through the inputs until they are all classified correctly. So let's do it


The next input vector is p₂. When it is presented to the network we find
```
	a = hardlim(₁wᵀp₂) = hardlim([2.0 1.2]|-1|)
					       | 2|
	  = hardlim(0.4) 
	  = 1
```


The target t₂ associated with p₂ is 0 yet the output a is 1. A class 0 vector was misclassified as a 1.

Looks like we have to apply a learning rule to update this vator. This time we want to move the weight vector ₁w away from the input, so we can simply change the addition from our rule to subtract rather than add. Like so:
```
	if t=0 and a=1, then ₁w(new) = ₁w(old) -p
```

if we apply this to the test problem we find
```
	₁w(new) = ₁w(old) -p₂ = |2.0| - |-1| = | 3.0|
				|1.2|   | 2|   |-.08|
```


Now, we present the third vector p₃
```
	a = hardlim(₁wᵀp₃) = hardlim([3.0 -0.8]| 0|)
					      |-1|
	  = hardlim(0.8)
	  = 1
```


The current ₁w results in a decision boundry that misclassifies p₃. We already have a rule for this, so ₁w will be updated again
```
	₁w(new) = ₁w(old) -p₃ = | 3.0| - | 0| = |3.0|
				|-0.8|   |-1|   |0.2|
```


This gives us the following result


<img src="img/img15.png" alt=" " width="600"/>


As we can see the Perceptron has now learned to classify the three vectors properly. If we present any of the input vectors to the neuron, it will output the correct class for that input vector.


this brings us to the final rule... If it's not broken, don't fix it
```
	if t=a, then w(new) = ₁w(old)
```

Here are the 3 rules which cover all possible combinations of output and target values

```
	if t=1 and a=0, then ₁w(new) = ₁w(old) +p
	if t=0 and a=1, then ₁w(new) = ₁w(old) -p
	if t=a, then w(new) = ₁w(old)
```


Now, lets see this in action by coding a preceptron class from scratch


# Perceptron from Scratch

Here is the class of perceptron



```
import numpy as np


class Perceptron:
    def __init__(self, learning_rate = 0.01, num_iters = 1000):
        self.lr = learning_rate
        self.n_iters = num_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # init weights
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                update = self.lr * (y_[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, 0)

```

We can test it with the following code

```
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from perceptron import Perceptron

def accuracy(y_true, y_pred):
    # Return the accuracy of the model
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


# Get datasets as blobs from sklearn
X, y = datasets.make_blobs(n_samples=150, n_features=2, centers=2, cluster_std=1.05, random_state=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Create a perceptron
p = Perceptron(learning_rate=0.01, num_iters=1000)
# Fit the traning data
p.fit(X_train, y_train)
# Predict the test labels
predictions = p.predict(X_test)

# Calculate the accuracy
print("Perceptron classification accuracy", accuracy(y_test, predictions))


# Plot the data

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.scatter(X_train[:,0], X_train[:,1], marker='o',c=y_train)

x0_1 = np.amin(X_train[:,0])
x0_2 = np.amax(X_train[:,0])

x1_1 = (-p.weights[0] * x0_1 - p.bias) / p.weights[1]
x1_2 = (-p.weights[0] * x0_2 - p.bias) / p.weights[1]

ax.plot([x0_1, x0_2], [x1_1, x1_2], 'k')

ymin = np.amin(X_train[:,1])
ymax = np.amax(X_train[:,1])
ax.set_ylim([ymin-3,ymax+3])


plt.show()

```


As we can see the Perceptron is working perfectly
```
 Perceptron classification accuracy 1.0
```
<img src="img/img16.png" alt=" " width="600"/>


* The full code can be [found here](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/blob/main/Machine-Learning-Algorithms/neural_networks/perceptron/perceptron.py)
* With tests [here](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/blob/main/Machine-Learning-Algorithms/neural_networks/perceptron/perceptron_tests.py)

