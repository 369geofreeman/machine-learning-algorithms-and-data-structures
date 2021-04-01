# PyList Concatenate

class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None] * size
        self.numItems = 0
        self.size = size

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if index >= 0 and index < self.numItems:
            return self.items[index]

        raise IndexError("PyList index out of range")

    def __setitem__(self, index, val):
        if index >= 0 and index < self.numItems:
            self.items[index] = val
            return

        raise IndexError("PyList assignment index out of range")

    def __add__(self, other):
        result = PyList(size=self.numItems+other.numItems)

        for i in range(self.numItems):
            result.append(self.items[i])

        for i in range(other.numItems):
            result.append(other.items[i])

        return result





