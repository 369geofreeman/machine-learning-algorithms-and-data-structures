# The pyList constructor


class pyList:
    def __init__(self, contents=[], size=10):
        '''
        The  contents allow the programmer to construct a list with
        the initial contents of this value. The initial_size
        lets the programmer pick a size for the internal size of the
        list. This is useful if the programmer knows he/she is going
        to add a specific number of items right away to the list.
        '''
        self.items = [None] * size
        self.numItems = 0
        self.size = size

        for e in contents:
            self.append(e)



