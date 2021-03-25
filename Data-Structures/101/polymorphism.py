# Ploymorphism
# ---

# The word polymorthic literally means many forms.
# As this concept is applied to computer programming, the idea is that there can be many ways that a particular behaviour might be implimented. Usually this means, at least with OOP, that we will be breaking up many of our commands into class structures.
# We will show this below using Turtle and creating graphic command classes.


'''
Each of the command classes below hold information for one of the
types of commands found in a graphics file. For each command there must
be a draw method that is given a turtle and uses the turtle to draw
the object. By having a draw methodfor each class, we can
polymorphically call the right draw method when traversing a sequence of
these commands. Polymorphism occures when the 'right' draw method gets
called without having to know which graphics command it is being called on.
'''

import turtle


class GoToCommand:
    # Here the constructor is defined with defult values for width and color.
    # this means we can construct a GoToCommand object as GoToCommand(10,20),
    # or GoToCommand(10,20,5), or GOToCommand(10,20,5,"yellow").
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)


class CircleCommand:
    def __init__(self, radius, width=1, color='black'):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()


class EndFillCommand:
    def __init__(self):
        # Passes a statement placeholder and does nothing. We have nothing
        # to initiate in this classs because all we want is the polymorphic
        # behaviour of the draw method.
        pass

    def draw(self):
        turtle.end_fill()


class PenUpCOmmand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()


class penDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()









