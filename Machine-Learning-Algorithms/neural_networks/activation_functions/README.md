# Activation Functions

Below is a collection of activation functions with a brief description of their use case and how they fit well for the required problem.


## Contents

* [Quick Reference Table](#quick-referance-table)
* [Hard Limit / Binary Step](#hard-limit-binary-step)
* [Linear Function](#linear-function)
* [Sigmoid Function](#sigmoid-function)



## Quick Reference Table

Add table here




## Hard Limit / Binary Step

The hard limit or binary step activation function sets the output of the neuron to 0 if the function argument is less than 0, or 1 if the argument is greater than or equal to 0.

**Best used for** When we are trying to create a binary classifier due to the binary output. Ie, Although it should be noted that this can be problematic with backpropagation due to the zero output, calculating the derivative of f(x) with respect to x will be equal 0


**Mathematically:**
```
	f(x) = 1, x>=0
     	     = 0, x<0
```

This can be coded as a simple if else statement in python

**Python**
```
	def binary_step(x):
    	    return 0 if x < 0 else 1
```

**A visulisation of the Hard Limit / Binary Step activation function**


<img src="img/binary_step.png" alt=" " width="700"/>



## Linear Function

The Linear function gives an output based on the input. That is it takes the inputs, multiplied by the weights for each neuron, and creates an output signal proportional to the input.

It should be noted we can not use backpropagation with this activation function.
Also, no matter how many layers in the neural network, the last layer will be a linear function of the first layer. Basically it turns the neural network into just one layer.

**Mathematically**
```
	f(x)=ax
```

**Python**
```
	def linear_function(x):
    	    return 4*x
```


**A visulisation of the Linear activation function**

<img src="img/linear_function.png" alt=" " width="700"/>



## Sigmoid Function

The popular sigmoid takes in any input and squashes the output into the range 0 to 1. It's commonly use in multilayer networks that are trained using backpropergation.


**Mathematically**
```
	       1
	a =  ------
	      1+e⁻ⁿ
```

**Python**
```
	def sigmoid_function(x):
             return (1/(1 + np.exp(-x)))
```

**A visulisation of the Sigmoid activation function**

<img src="img/sigmoid_function.png" alt=" " width="700"/>





