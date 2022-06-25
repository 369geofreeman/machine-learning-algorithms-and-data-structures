'''
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are 
performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a 
circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, 
once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using 
the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- int Front() Gets the front item from the queue. If the queue is empty, return -1.
- int Rear() Gets the last item from the queue. If the queue is empty, return -1.
- boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFull() Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 
'''


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue = []

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if value is not None and not self.isFull():
            self.queue.append(value)
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.queue.pop(0)
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[0]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.queue == []

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
