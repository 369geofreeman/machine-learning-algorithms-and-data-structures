# Logistic Regression



### Contents

  * [Classification Introduction](#classification-introduction)
  * [How not to solve a classification problem](#how-not-to-solve-a-classification-problem)
  * [Hypostesis Representation](#hypostesis-representation)
  * [Decision Boundry](#decision-boundry)
  * [Non Linear Boundries](#non-linear-boundries)
  * [Logistic Regression Model](#logistic-regression-model)


## Classification Introduction


A classificatiojn problem is where the variable y, that you want to predict, is valued.
Classification is the process where computers group data together based on predetermined characteristics - we know this as supervised learning.
A classic example of this is spam detection in email. We can train a machine learning algorithm with a set of spam-like emails labelled as not-spam. This way our algorithm learns what might be a spam email and dispose of it before it reaches our inbox.

Classification is great with big data and is commonly used to make decissions in governments, economics, medicine and even helps to solve problems with online fraud, classifying stolen credit card information or stolken passwords to name a few. 


All of these problems have one thing in common, they are 'yes' or'no' answers, true or false, 0 or 1. We can view this prediction as y:
```
	y ∈ {0,1}

0 = negative class
1 = possitive class
```

We can also use classification  for multi-class problems too, which we will get to soon. But for now they look something like this
```
	y ∈ {0,1,2,3}
```


**So how do we build a classification algorithm?**

Lets look at a traning set for defining whether a tumor is malignant or benign


<img src="img/img1.png" alt="classification img" width="700"/>


Notice the malignancy takes on only two values, zero or no and one or yes


## How not to solve a classification problem


A basic idea to solve this would be to use linear regression and try to figure out how to fit a straight line to the data. Lets try it and see what happens

So we can use our linear regression hypothesis:
```
	h𝜣(x) = 𝜣ᵀx
```

And we get the following result


<img src="img/img2.png" alt="classification img" width="600"/>


Then, since we know that the data is either 0 or 1, we could apply a threshold on the classifier outputs at 0.5 that is at the vertical axis at 0.5. 
Then if the hypothesis outputs a value greater than 0.5 we will say y=1. Likewise, if a value is output less than 0.5, we will say y=0

This looks something like this


<img src="img/img3.png" alt="classification img" width="600"/>


Now, we can clearly see a seperation from the malignant and benign tumor data points. So now we could just assign everything to the right of the line as 1 and 0 to the left of the line. This would correctly classify all of our points given the data so problem solved right?

Well, while this works with the ideal data used here, unfortuantly data in the real world might not be so kind to us. Which is more often the case.

For example, if we were to have a data set like below where the data points are more spread out

<img src="img/img4.png" alt="classification img" width="600"/> 

We can see where we might run into problems. We can clearly see some of the possitive data points will be missclassified as benign tumors which is obviously not good.
So although linear regression is great for a lot of tasks, tasks like this one are much better suited so something more advanced like a classification problem.

And that brings us to an algorithm that fits this well... The **Logistic Regression** algorithm, where the predictions are always between zero and one
```
	0 < h𝜣(x) ≦ 1
```


## Hypostesis Representation

Now lets look at the function we will use when working with a classification problem:
```
	Logistic Regression Problem:
	want 0 ≦ h𝜣(x) ≦ 1
```


So, we want our classifier to output values between 0 and 1, and we need a hypothesis that satisfies this property 

Ourhypothesis is similar to that of linear regression except that we have a function g()
```
	h𝜣(x) = g(𝜣ᵀx)
```

and g is equal to
```
	g(z) = 1/1+e^-z
z is a real number
```

This is known as the Sigmoid Function or the Logistic Function


An alternative way we can write this sigmoid function is 
```
		    1
	h𝜣(x) =  --------
		 1+e^-𝜣ᵀx
```


Let's take a look at what this looks like plotted on a graph



<img src="img/img5.png" alt="classification img" width="600"/>

Notice how z goes to minus infinity as g(z) approaches 0, and as z approaches positive infinity, g(z) approaches 1.

And because g(z) upwards values are between 0 and 1, we also have that h(x) must between 0,1.

Finally, given this hypothesis representation, what we now need to do is fit the parameters 𝜣 to our data, which we will get to later.

But forst , let's find out more about how we can interpret the output of our hypothesis h(x)


For examp,e, if we are using the tumor classification example, and
```
	x = |x₀| = |     1    |
	    |x₁|   |tumor size|

h𝜣(x) = 0.7
``` 

Then we can tell the patient that there is a 70% chance of the tumor being malignant.

More mathmatically this can be viewed as
```
	h𝜣(x) = p(y=1|x;𝜣)
```
Which can be read as "Probability that y=1, given x, parameterized by 𝜣"


But since this is a classification task, we know that y can only equal y=0 or y=1

so we use
```
	p(y=0 | x;𝜣) = 1 - p(y=1 | x;𝜣)
```

Which basically says it is a one if we are above half and zero otherwise


## Decision Boundry


One quick thing to note here is, given our hypothesis for linear regression
```
	h𝜣(x) = g(𝜣ᵀx)
	⟶  g(z) = 1/1+e^-z
```

If we where to predict y=1 so h𝜣(x) ≧ 0.5, that would mean 𝜣ᵀx ≧ 0. And if y=0 so h𝜣(x) < 0.5, then 𝜣ᵀx < 0. Because as we remember, 𝜣ᵀx is a range between -1, +1 generally.

now let's use this to better understand how the hypothesis of logistic regression makes those decissions.

Say we have a traning set like this

<img src="img/img6.png" alt="classification img" width="600"/>

And our hypothesis is:
```
	h𝜣(x) = g(𝜣₀+𝜣₁x₁+𝜣₂x₂)
```
And say we choose the following parameters

* 𝜣₀ = -3
* 𝜣₁ = 1
* 𝜣₂ = 1

So our parameter vector will equal
```
	    |-3 |
	𝜣 = | 1 |
	    | 1 |
```

Now let's try and figure out where a hypothesis would end up predicting y=1 and where it would end up predicting y=0

So, we know the probability of y=1 whenever 𝜣ᵀx > 0.

So, from our parameter vector, if we take -3, we can predict y=1 if:
```
y=1 if
	-3+x₁+x₂ ≧ 0
	------------
	    𝜣ᵀx
```

Let;s see what this means on our chart. Basically, x₁+x₂ = 3 is the equation for a line, and we can draw that on our graph like so


<img src="img/img7.png" alt="classification img" width="600"/>

And so if y=1 (-3 + x₁ + x₂ ≧ 0) then it will be classified to the right of the line, and if y=0 (-3 + x₁ + x₂ < 0) then it will be classified to the left of the line like below


<img src="img/img8.png" alt="classification img" width="600"/>

And the line that seperates the data (drawn in green) is known as the **desision boundry**

And our decision boundry (x₁ + xx₂ = 3) corrisponds to 0.5 exactly.



## Non Linear Boundries

Now lets look at some data points that can't be solved linearly, for example


<img src="img/img9.png" alt="classification img" width="600"/>


As we can see, no straight line can seperaste this data.

One way we could solve this might be to add higher order polynomeal terms to the features.

Let's say our hypothesis now looks like this, where we added 2 extra features, x₁² and x₂²
```
	h𝜣(x) = g(𝜣₀ + 𝜣₁x₁ + 𝜣₂x₂ + 𝜣₃x₁² + 𝜣₄x₂²)
```

So we now have 5 parameters, 𝜣₀ ⟶  𝜣₄. And for now let's set them like so

* 𝜣₀ = -1
* 𝜣₁ = 0
* 𝜣₂ = 0
* 𝜣₃ = 1
* 𝜣₄ = 1

So our feature vector will be
```
	    |-1 |
	𝜣 = | 0 |
	    | 0 |
	    | 1 |
	    | 1 |
```

And we know our hypothesis is equal to 1 when; predict 1: y=1 if -1 + x₁² + x₂² ≧ 0

Or, in fact if we shift the 1 to the right, we get
```
	predict y: y=1 if x₁² + x₂² ≧ 1
```

And this equation now looks familiar (x₁² + x₂² = 1), most likely because it is the equation for a circle.
Now this will seperate our data very nicely. Everything outside the decision boundry circle is 1 and everything inside it is 0



<img src="img/img10.png" alt="classification img" width="600"/>


So basically, with more complicated data we can use more complicated boundries in the form of polynomials to seperate our data



## Logistic Regression Model


**Cost function**


Now we need to find a way to fit the parameters of 𝜣 for the logistic compression.

We'll use a cost function to fit the parameters

What we are looking for is a cost function that is convex. So a nice smooth curve that has one local minima like below


<img src="img/img11.png" alt="classification img" width="500"/>

Now, because of our sigmoid function being non-linear, we can't use a square error cost function otherwise we will end up with it being non-convex

So what we will our cost function look like?

```
			{ -log(h𝜣))     if y = 1
	cost(h𝜣(x),y) = {
			{ -log(1-h𝜣(x)) if y = 0
```

This basically means that the penalty that the algorithm pays, say if h(x) = 0.7 for instance, and that would be y=1, then -log(h𝜣(x)). 
The penalty it pays it higher the further away from 1 it is, in this case 0.3

To better visualise this, let's look at it plotted below


<img src="img/img12.png" alt="classification img" width="600"/>


So above is our cost function for y=1 (-log(h𝜣(x)))


Notice how as h(x) approaches 0, it goes on for ∞. Equally if we were to plot for y=0, as h𝜣(x) approaches 1, it would go on for ∞ too.

If we were to, for instance predict h𝜣(x) = 0 (for the graph above where y=1), we would end up paying a very large cost. The further  from 0 it is, the higher the cost, as seen in the graph.

Inversly, if y=0, then the further to 1 we approach with our prediction h𝜣(x), the more we will penalise the result.

Some examples are:

```
	- if h𝜣(x) = y, then cost(h𝜣(x),y = 0 (for y=0 and y=1)
	- if y = 0, then cost (h𝜣(x), y ⟶  ∞ as h𝜣 ⟶  0
	- Regardless of whether y=0, if h𝜣(x) = 0.5, then cost(h𝜣(x),y) > 0
``` 























