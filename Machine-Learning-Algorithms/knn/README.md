# K-Nearest Neighbours


### Code

  ---


## Contents
  * [Overview](#overview)
  * [Algotithm](#algotithm)




## Overview


k nearest neighbor (Knn) is a simple classification algorithm that belongs to the family of instance-based learning, or lazy learning methods. 
This means that it doesn't use traning data points to make genralisations, meaning the training phase is very minimal or more commonly, non-existant which makes it very fast.

A drawback of this is the learning data is kept for testing, which can be expensive to compute given large data sets.
Knn works by finding similarities in the data. It's concidered a clustering algorithm based on the idea that samples that are close with respect to a predefined distance metric are also similar

<img src="img/img1.png" alt=" " width="700"/>

In the above image we have binary data set consisting of red stars and green triangles. The data point we are trying to classify is in the middle. We can see the closest 3 data points or closest 7 data points to the data point we are trying to classify represented with the dotted lines.

Knn also doesn't make any assumptions on the underlying data distribution. Ie, it's non parametric. 
This can be very useful and is one of the main strengths Knn has. In the real world, practical data tends not to obey the typical theoretical assumptions made (eg gaussian mixtures, linearly seperable etc). So a non parametric algorithm can be very useful here

We can expect to find k nearest neighbor used for text categorisation (as will see later) or text mining as a popular use case but it is used in a wide variety of instances. For example in agriculture for the evaluation of forest inventoring, forecasting the stock market / trading futures in finance and various medical practices. 

Lets see how it works



## Algotithm

K nearest neighbor is actually a very simple algorithm. Basically, given N traning vectors, Knn identifies the K nearest neighbors of 'c' regardless of labels


<img src="img/img2.png" alt=" " width="600"/>

Here we can see 'c' as our data point we are trying to classify, either it will be a red x or a green circle

Now firstly, we need to set K to a fixed number so we know how many neighbors we want to visit and compare 'c' to. 
We will usually set K to an odd number to avoid an even number of data sets which could create a tie leaving us witout a definite answer as to wht to classify 'c' as. 

So it basically works like this. If, for instance K=5, we will visit the 5 closest points (circled below)


<img src="img/img2.png" alt=" " width="600"/>





















