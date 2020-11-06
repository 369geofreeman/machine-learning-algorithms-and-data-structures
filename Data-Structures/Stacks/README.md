# Stacks

  * [Stack](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/blob/main/Data-Structures/Stacks/code-examples/Stack.py): The stack class
  * [Reversing data](): An example of reading data from a text file and reversing it into another text file using our Stack class
  * [Matching Delimiters](): An example of checking the delimiters in a mathmatical expresion are balances using our Stack class


### Contents

* [Overview](#Overview)
* [Why Stacks?](#why-stacks)
* [Stack Methods](#stack-methods)
* [Big O Time Complexity](#big-o-time-complexity)
* [Implementing a Stack](#implementing-a-stack)
* [Reserving Capacity](#reserving-capacity)
* [Stacks in Practice](#stacks-in-practice)


## Overview

A stack is a collection of onjects that are inserted and removed according to the **Last in First out** or (**LiFo**) principle.
This means that we can stack as many objects as we like in our stack but removing them will have to be in the reversed order from how they were inserted

A common way to think of it, is as a stack of plates in a cafeteria that are spring loaded. When we take a plate we take or '**pop**' it from the top of the stack. When we place a new plate on the stack we place or '**push**' it on the top making it the new top or last in plate.

But why are stacks useful as data structures in computer science? Lets find out



## Why stacks?

A more concreate example in computer science would be a web browser, or more specifically how they store the address of the pages you have visited in a stack. Each time we visit a new page or site , it's address is '**pushed**' onto the '**stack**' of addresses.
Likewise, when we press the back button, the current address is '**popped**' off of the stack and we are left with the previous page (address) we visited.

Text editors use a similar system to allow us to 'undo' what we have written, reverting the document to a previous state.

Basically, a stack lets you manage your data in a particular way. Other use cases inclue, reversing order, testing symmetry and recursion. We'll explore some of these below.


## Stack Methods

Stacks are amounge one of the simpliest data structures and they require very few methods. In fact the only two real methods for a stack are **push** (to add an object to the top of the stack) and and **pop** (to remove an object from the top of the stack). Other methods in our stack class will be for simply viewing elements of the stack or checking to see if it is empty.
But we shouldn't underestimate their importance as they are used for many sophisticated data structures and algorithms. 
 
Let's take a look at a series of stack operations on an initially empty stack. We will use the two main methods:
  * **S.push()**: Add an element
  * **S.pop()**: Remove an element
As well as adding a few more for convenience:
  * **S.top()**: View the top of object of the stack without adding or removing anything
  * **S.is_empty()**: Return True if the stack is empty
  * **len(S)**: return the number of elements in the stack


Lets look at these methods in action


| Operation    | Return Value | Stack Contents |
|--------------|--------------|----------------|
|   S.push(5)  |       -      |       [5]      |
|   S.push(3)  |       -      |      [5,3]     |
|    len(S)    |       2      |      [5,3]     |
|    S.pop()   |       3      |       [5]      |
| S.is_empty() |     False    |       [5]      |
|    S.pop()   |       5      |       []       |
| S.is_empty() |     True     |       []       |
|    S.pop()   |    'error'   |       []       |
|   S.push(7)  |       -      |       [7]      |
|   S.push(9)  |       -      |      [7,9]     |
|    S.top()   |       9      |      [7,9]     |
|   S.push(4)  |       -      |     [7,9,4]    |
|    len(S)    |       3      |     [7,9,4]    |
|    S.pop()   |       4      |      [7,9]     |
|   S.push(6)  |       -      |     [7,9,6]    |
|   S.push(8)  |       -      |    [7,9,6,8]   | 




## Big O Time Complexity


|   Operation  | Running Time |
|:------------:|:------------:|
|  S.look_up() |     O(n)     |
|    S.pop()   |     O(1)     |
|   S.push()   |     O(1)     |
|    S.top()   |     O(1)     |
| S.is_empty() |     O(1)     |
|    len(s)    |     O(1)     |



## Implementing a Stack


For our initial implementation of a stack class, we will use a python list for storage.
This is initilised in the constructure as self.data = []

```
class Stack():
    """LIFO stack implementation using a python list as underlying storage"""

    def __init__(self):
        # create an empty stack
        self._data = []

    def __len__(self):
        # Return the number of elements in the stack
        return len(self._data)

    def is_empty(self):
        # Return True if stack is empty
        return len(self._data) == 0

    def push(self, e):
        # Add element e to the top of the stack
        self._data.append(e)

    def top(self):
        # Return (but does not remove) the element at the top of the stack
        # Raise Empty exception if the stack is empty

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        # Remove and return the element from the top of the stack
        # Raise Empty exception if the stack is empty

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

```

The code for this can be found [here](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/blob/main/Data-Structures/Stacks/code-examples/Stack.py) where we will use this class for the next examples where we test our stack to solve some problems.


## Reserving Capacity


Before we jump into the examples it's worth mentioning about reserving memory capacity. 
in some instances we might want to reserve memory cap[acity if we think our stack will be particularly large, or if know teh final size it will be.

In our example above we started with an empty list which could append n items. But it can be more efficient to construct a list with an initial length in mind given we know the data being used



## Stacks in Practice


**1) Reversing Data**

For this example we will open a text file, store the contents line by line in our imported stack class and then return the lines one by one in reverse order to a new text file.
This is a classic example of the **LIFO** protocol.

[Click here](https://github.com/369geofreeman/machine-learning-algorithms-and-data-structures/blob/main/Data-Structures/Stacks/code-examples/reversing-data.py) to view the code with test examples
















