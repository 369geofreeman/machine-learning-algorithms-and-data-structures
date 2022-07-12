# # content of test_sample.py
# def inc(x):
#     return x + 1


# def test_answer():
#     assert inc(3) == 4


"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        # self.MAX = 10000
        # self.table = [None for _ in range(self.MAX)]
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        h = self.calculate_hash_value(string)
        self.table[h] = string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        h = self.calculate_hash_value(string)

        if self.table[h]:
            return h
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        h = int(str(ord(string[0])) + str(ord(string[1])))
        return h


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
