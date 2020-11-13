# K-Nearest Neighbours


### Code

  ---


## Contents
  * [Overview](#overview)
  * [Algotithm](#algotithm)
  * [Distance](#distance)
  * [KNN From Scratch](knn-from-scratch)
  * [Advantages and Disadvantages](#advantages-and-disadvantages)
  * [Applying KNN to the MNist Dataset](applying-knn-to-the-mnist-dataset)

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


For the above image, we can see there are 4 red x and 1 green circle that fall into the range of K nearest neighbors (given K=5).

So given this, 'c' is most likely a red x and will be classified as one.

Now the next logical question is how do we get the distances from 'c' to find the closest data points


## Distance

Well, most commonly the default metric is either euclidean **sqrt(sum((x-y)^2))** or the Minkowski **sum(|x-y|^p)^(1/p))** distance. On a side note, if we set the parameters of Minkowski equal to 1, it will produce the equivalent of using standard Manhatton distance, if we set it to 2 it will produce the equivalent of using standared Eclidean distance.

Heres a full list of distance metrics that the sklearn library provides

| identifier    | class name          | args    | distance function            |
|---------------|---------------------|---------|------------------------------|
| “euclidean”   | EuclideanDistance   |         | sqrt(sum((x - y)^2))         |
| “manhattan”   | ManhattanDistance   |         | sum(\|x - y\|)               |
| “chebyshev”   | ChebyshevDistance   |         | max(\|x - y\|)               |
| “minkowski”   | MinkowskiDistance   | p       | sum(\|x - y\|^p)^(1/p)       |
| “wminkowski”  | WMinkowskiDistance  | p, w    | sum(\|w * (x - y)\|^p)^(1/p) |
| “seuclidean”  | SEuclideanDistance  | V       | sqrt(sum((x - y)^2 / V))     |
| “mahalanobis” | MahalanobisDistance | V or VI | sqrt((x - y)' V^-1 (x - y))  |


It's important to note that a larger P value produces shorted measures.
Also, if we set P=1, all components are taken into account in the same way.

Finding the most appropriate value for P requires a pre-analysis of the data set and full domain knowledge. It's always recommended to test different values, comparing the results and picking the one which best represents the structure of the underlying problem.

One example of the algorithm used to compute the nearest neighbours is based on a data structure called the ball tree.
A ball centered on a sample, X, is formally equivalent to Nr(X), where r defines the radius. therefour, the tree is built by nesting smaller balls (in terms of radius) into larger ones.

Lets see this all together as we impliment K nearest neighbors from scratch


## KNN From Scratch


===== Coming soon ======




## Advantages and Disadvantages



**Advantages**

 * Simplicity
 * Fast convergance time
 * Can be useful for regression and classification
 * No traning period due to it being a _lazy learner_
 * New data can be added seamlessly


**Disadvantages**

 * Gets very expensive to compute as the data set gets larger
 * Difficault to use with higher dimensions
 * Very sensitive to noisy data
 * Accuracy depends on quality of the data



## Applying KNN to the MNist Dataset


Let's test k nearest neighbors using the famous MNist handwritten digests dataset.
We can import import this from sklearn . The data set containes 1,797 greyscale 8x8 images representing the digits from 0-9

Here is an example from the dataset

<img src="img/img4.png" alt=" " width="800"/>

To find out more about it follow [this link](http://yann.lecun.com/exdb/mnist/)

We will use Knn to cluster the data together and find the enarest neighbors of noisy samples.

Lets load in the data set and scale it


```
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler

digits = load_digits()

ss = StandardScaler(with_std=False)
X = ss.fit_transform(digits['data'])
```

We set _"with_std=False"_ to limit the process to the mean.

After scaling the samples, the values are bound between -1.0 & 1.0

Now we can instantiate the NearestNeighbors class and fit the model.

```
from sklearn.neighbors import NearestNeighbors

Knn = NearestNeighbors(algorithm="ball_tree", n_neighbors=25, leaf_size=30)

```

Now the model is fit we can expect the digits belonging to the same class will have very short distances.
We can apply Gaussion Noise to the sample because the digits are handwritten, the deformation spread uniformly around a mean value (which should be a perfect representation of each specific digit)

```
import numpy as np

x_noise = x[50] = np.random.normal(0.0, 1.5, size=(64, ))

```

We can now use the Kneighbors function to retrieve the indexes of 25 nearest neighbors of the sample, setting the _"return_distance=True"_ allows us to also obtain the distances in ascending order.

```
distances, neighbors = Knn.kneighbors(x_noise.reshape(1, -1), return_distance=True)

print(distances[0])
```

The full code can be [found here]()

The smallest distance isn't very small because of the noise, but by plotting the results we can see a confirmation of the results.








