# Solving XOR with a Neural Network



### Contents

  * [The XOR Problem](#the-xor-problem)
  * [Neural Networks](#neural-networks)
  * [Manual Testing](#manual-testing)
  * [Coding and the Learning Algorithm](#coding-and-the-learning-algorithm)



## The XOR Problem


An XOR (exclusive OR gate) is a classic problem in the history of neural network research. 
It is the problem of predicting the outputs of XOR logic gates given two binary inputs.

An XOR logic gate works by giving a true output only when the inputs are different from one another. 
With x1 and x2 being the inputs and y being the output, it works as follows:

| INPUT |      | OUTPUT |
|:-----:|:----:|:------:|
|   x1  |  x2  |    y   |
|   0   |   0  |    0   |
|   0   |   1  |    1   |
|   1   |   0  |    1   |
|   1   |   1  |    0   |


For instance if we feed it [0,0] we will get 0, [0,1] = 1 etc.

Back in the early days of AI research, Marvin Minsky and Seymour Papert proved this could not be solved due to, at the time, only having a single layer neural networks, notibly the perceptron.
 It is noted that this helped towards the _"AI winter"_ of the 1980's where advancements underperformed to expectations leading to a change in the way people thought about AI

The perceptron algorithm (invented 1958 by Frank Rosenblatt) is a linear classifier for binary classification. It is used to decide whether or not an input, represented by a vector of numbers, belongs to some specific class decide whether or not an input, represented by a vector of numbers, belongs to some specific class.
Despite initally seeing very promising, it was quickly proved that perceptrons (at least single layer perceptrons) coulkd not be trained to recognise many classses of paterns. One being the XOR problem.

To visulalise this let's graph it. First lets see some examples of a problem that can be linearly seperated.

<p align="middle">
  <img src="img/img1.png" alt=" " width="300"/>
  <img src="img/img2.png" alt=" " width="300"/>
  <img src="img/img3.png" alt=" " width="300"/>
</p>

As we can see, a linear classifier solves all of these examples with ease. But what about this one where we use our points from the XOR table?


<img src="img/img4.png" alt=" " width="500"/>

No linear classifier can solve this. Ie, there is no straight line that can serperate this data.

We'll need to train a neural network to classify the input patterns accordingly and seperate this data using decision boundries.

It's good to note that the type of decision boundry that the neural network can learn is determined by the number of hidden layers the network has. If there are no hiffen layers, like in the case of the single layer perceptron, then it can only learn linear problems.



## Neural Networks


A basic neural network with one hidden layer looks like this 

<img src="img/img5.png" alt=" " width="800"/>


This is a basic neural network that has a single layer. neural networks can get a lot more complicated than this one but this is perfect for our XOR problem.

if we apply our problem to the above neural network, it looks like this


<img src="img/img6.png" alt=" " width="800"/>


* Input = (x₁, x₂)
* Hidden layer = (h₁, h₂)
* Output layer = (y)
* Weights for h1 (hidden layer) = (20, 20)
* Weights for h2 (hidden layer) = (-20, -20)
* Bias for h1 = (-10)
* Bias for h2 = (30)
* Weights for output (y) = (20, 20)
* Bias for output (y) = (-30)



Note that for this initial demonstration we selected the values of our weights and biases knowing they will produce the desired outcome.
 In reality we start with random values an iterate until conversion, which we will see in the coding implementation section next.

But first, let's test this neural network by manually running through it with our pre-selected values.

## Manual Testing


So the initial inputs from our XOR problem are as follows
```
	[0, 0]
	[0, 1]
	[1, 0]
	[1, 1]
```

We will insert each of these into the neural network by passing them to the inputs one by one. The neurons in the network will be using the sigmoid function because it's a continuious functin that outputs avalue between 0 - 1

```
Sigmoid = σ()

	[0,0] = σ(20*0+20*0-10) ≈ 0 ; σ(-20*0-20*0+30) ≈ 1 ; σ(20*0+20*1-30) ≈ 0
	[1,1] = σ(20*1+20*1-10) ≈ 1 ; σ(-20*1-20*1+30) ≈ 0 ; σ(20*1+20*0-30) ≈ 0
	[0,0] = σ(20*0+20*1-10) ≈ 0 ; σ(-20*0-20*1+30) ≈ 1 ; σ(20*1+20*1-30) ≈ 1
	[0,0] = σ(20*1+20*0-10) ≈ 0 ; σ(-20*1-20*0+30) ≈ 1 ; σ(20*1+20*1-30) ≈ 1
```

As we can see from the outputs it works. Remember the rules of XOR are, if the parameteres are different we get back a possitive (1), else negative (0).

So from our algorithm, when we passed our inputs, we got these outputs
```
	[0,0] ≈ 0
	[1,1] ≈ 0
	[0,1] ≈ 1
	[1,0] ≈ 1
```

So what this is doing is, if we look at the first neuron (h₁), it's performing a logical OR by outputinga 1 whenever at least one of the inputs is a 1.
The second neuron (h₂) is like the flipside of a logical OR, it outputs a 1 as long as one of the units is a 0, else it will ouput a 1.
And (y) is basically doing an AND, it wants both inputs to be on for the output to be on. If they are both 1 we get back a 1, else 0.


So thats the logic behind solving XOR with a neural network. Another way to think about it is; Remember each one of the units is a logistic unit and a unit has a hyperplane associated with it.
Now, what would a hyperplane for (h₁) look like?
Well, if we use the same values from earlier to visualise this, 20 + 20 - 10, it would go through [1,1], but the bias is a little smaller, so it offsets the hyperplane pulling it a little to the left like so


<img src="img/img7.png" alt=" " width="600"/>

And now if we add the hyperplane for (h₂)

<img src="img/img8.png" alt=" " width="600"/>


So what this classifier is doing is putting two hyperplanes into the space, and (y) is looking for an intersection of these hyperplanes.

This is obviously a very basic introduction to neural networks but it's an important one. Historically it was a huge breakthrough in the development of AI, thus this is a very powerful idea. It means whatever region of space the positives occupy, we can bracket them with hyperplanes and combine them together to learn the decision boundry however complicated it might be.

Now we have a solid understanding of basic nerual networks and how to use them to solve XOR, let's impliment one using Python.


## Coding the Learning Algorithm









