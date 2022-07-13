# Graphs

Indepth look in to grapghs [here](https://algs4.cs.princeton.edu/40graphs/)

There are four important types of graph models:

- **Undirected graphs**: => with simple connections
- **Digraphs graphs**: => where the direction of each connection is significant
- **Edge-weighted graphs**: => where each connection has an software associated weight
- **Edge-weighted digraphs**: => where each connection has both a direction and a weight

Connectivity in a directed graph is a bit more complicated than in an undirected graph. Let's look at some more definitions:

**Disconnected**
Disconnected graphs are very similar whether the graph's directed or undirected—there is some vertex or group of vertices that have no connection with the rest of the graph.

**Weakly Connected**
A directed graph is weakly connected when only replacing all of the directed edges with undirected edges can cause it to be connected. Imagine that your graph has several vertices with one outbound edge, meaning an edge that points from it to some other vertex in the graph. There's no way to reach all of those vertices from any other vertex in the graph, but if those edges were changed to be undirected all vertices would be easily accessible.

**Connected**
Here we only use "connected graph" to refer to undirected graphs. In a connected graph, there is some path between one vertex and every other vertex.

**Strongly Connected**
Strongly connected directed graphs must have a path from every node and every other node. So, there must be a path from A to B AND B to A.

### Edge list

An edge list is simply a list of edges that each contain two integers representing ID numbers for corresponding vertices. or put more simply; The inner lists are each a list that is showing two nodes that have an edge between them, and the edge list is the list that encompasses all the inner lists.

- The Edge list is 2 dimensional (2d)

```
Exp:

edge_list  [
    [0,2], [1,2]
    [1,3], [2,3],
]
```

### Adjancency List

And adjancency list is another way to represent edges in a graph. In an adjancency list the vertices normally have an ID number that corrisponds to the index in an array.
In our array each space is used to store a list of nodes that the node with that ID is adjacent to.

For example, the opening at index 0 (below), represents a vertex with an ID of 0. That vertext shares an edge with one node so oor reference is stored at the forst spot in the array `[1]`.

```
(0)----(1)           adjacency_list = [
      /  |                              [1], [0, 2, 3],
     /   |                              [1, 3], [1, 2]
   (3)--(2)                           ]
```

The adjacency list is also 2d.

### Adjancency Matrix

In computer science a matrix is a 2d array, but all the lists inside the array are the same length.

The Adjancency Matrix is similar to the Adjancency List. The indices in the outer array still represent the nodes IDs, and the list inside still represents which nodes are adjacent. However, these inner lists represent information in a slightly diffreent way. Before the list contained just the IDs of the adjacent nodes. Now the inner list has one slot for every node in the array, where node IDs map to array indices. If there is an edge between these two nodes a 1 goes into the array. If there is no edge then a 0 goes into the array.
The place in the matrix where the row number os equal the column number is almost always a 0. This value will only be a 1 if there was an edge that started and ended with the same node.

```
(0)----(1)           adjacency_matrix = [
      /  |                              [0, 1, 0, 0],
     /   |                              [1, 0, 1, 1],
   (3)--(2)                             [0, 1, 0, 1],
                                        [0, 1, 1, 0]
                                       ]
```
