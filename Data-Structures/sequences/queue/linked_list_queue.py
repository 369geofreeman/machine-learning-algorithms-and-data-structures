"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""


class Queue:

    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, head=None, tail=None):
        self.size = 0
        if head:
            node = self._Node(head)
            self.tail = node
            self.head = node
            self.size += 1
        else:
            self.head = head
            self.tail = tail

    def enqueue(self, new_element):
        node = self._Node(new_element)
        if self.size == 0:
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        self.head = node
        self.size += 1

    def peek(self):
        if self.tail:
            return self.tail.value

    def dequeue(self):
        current = self.tail
        if self.tail:
            self.tail = self.tail.prev
            self.size -= 1
        return current.value


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
