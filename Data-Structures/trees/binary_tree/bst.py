# Binary Search Tree


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """Inserts a new value into the tree"""
        curr = self.root
        parent = None

        if self.root is None:
            return Node(new_val)

        while curr:
            parent = curr

            if new_val < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        if new_val < parent.value:
            parent.left = Node(new_val)
        else:
            parent.right = Node(new_val)

        return self.root

    def search(self, find_val):
        """Searches for a value in the tree
        Returns True if in tree, False otherwise"""
        curr = self.root

        while curr:
            if curr.value == find_val:
                return True
            if curr.value > find_val:
                curr = curr.left
            else:
                curr = curr.right

        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
