# Accumulator pattern
# ---


# This pattern is in nearly every program we write. When using this pattern
# you initialise an accumulator beofre a loop and then inside the loop you
# you add to the accumlulator. For instance, appending to a list of squares.

# Here will use it for a graphic program


import turtle
from polymorphism import *


# This is our pyList class. it holds a list of our graphics commands

class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    ''' If we want to iterate over this sequence, we define the special method
    called __iter__(self). Without this we'll get "builtins.typeError: 'PyList'
    object is not iterable" if we try to write
    for cmd in seq:
    where seq is one of these sequences. the yield below will yield an
    element of the sequence and will suspend the execution of the for
    loop in the method below until the next element is needed. the abillity
    to yield each element of the sequence as needed is called "lazy" evaluation
    and is very powerful. It means that we only need to provide access to as
    many of these elements of the sequense as are necessary and no more'''

    def __iter__(self):
        for c in self.items:
            yield c


def main():
    filename = input("Please enter drawing filename: ")

    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, 'r')

    # Create a PyList to hold teh graphics commands that are
    # read from the file.
    graphicsCommands = PyList()

    command = file.readlines().strip()

    while command != '':

        # Now we must read the rest of teh record and then process it. Because
        # records are variable length, we'll use an if-elif to determine which
        # type of record it is and then we'll read and process the record.
        # in this progtam, processing the record means creating a command object
        # using one of the classes above and then adding taht object to our
        # graphicsCommand PyList object.

        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)

        elif command == 'circle':
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)

        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)

        elif command == 'endfill':
            cmd = PenUpCommand()

        elif command == 'pendown':
            cmd = PenDownCommand()

        else:
            # Raising an exception will terminate the program immediately
            # which os what we want to happen if we encounter an unknown
            # command. the RunTimeError exception is a common exception
            # to raise. The string will be printed whne the exception is 
            # printed
            raise RunTimeError('Unknown COmmand: ' + command)

        # Finnish processing the record by adding the command ro the sequence
        graphicsCommands.append(cmd)

        # read one more line to set up for the next time through the loop
        command = file.readline().strip()

    # This code iterates through the commands to do the drawing and
    # demonstrates the use of the __iter__(self) method in the
    # PyList class above.
    for cmd in graphicsCommand:
        cmd.draw(t)

    file.close()
    t.ht()
    screen.exitonclick()
    print('Program Execution Completed')


if __name__ == '__main__':
    main()










