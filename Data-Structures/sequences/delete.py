# PyList Delete

class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None] * size
        self.numItems = 0
        self.size = size

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        # O(1) time
        if index >= 0 and index < self.numItems:
            return self.items[index]

        raise IndexError("PyList index out of range")

    def __setitem__(self, index, val):
        # O(1) time
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return

        raise IndexError("PyList assignment index out of range")

    def __add__(self, other):
        # O(n) time
        result = PyList(size=self.numItems+other.numItems)

        for i in range(self.numItems):
            result.append(self.items[i])

        for i in range(other.numItems):
            result.append(other.items[i])

        return result

    # This method is hidden since it starts with two underscores.
    # it is only avaliable to the class to use
    def __makeroom(self):
        # Increase list size by 1/4 to make more room.
        # Add one in case for some reason self.size is 0.
        newlen = (self.size // 4) + self.size + 1
        newlst = [None] * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]

        self.items = newlst
        self.size = newlen

    def append(self.item):
        # O(1) time
        if self.numItems == self.size:
            self.__makeroom()

        self.items(self.numItems) = item
        self.numItems += 1

    def insert(self, i, e):
        # O(n) time
        if self.numItems == self.size:
            self.__makeroom()

        if i < self.numItems:
            for j in range(self.numItems-1, i-1, -1):
                self.items[j+1] = self.items[j]

            self.items[i] = e
            self.numItems += 1
        else:
            self.append(e)

    def __delitem__(self.index):
        # O(n) time
        for i in range(index, self.numItems-1):
            self.items[i] = self.items[i+1]
        self.numItems -= 1


