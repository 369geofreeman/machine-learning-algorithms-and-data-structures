# operator overloading

# Python suports opperator overloading, if you define a method for your class with a name that is operator overloaded, your classwill support that operator as well.

# For instance, writing x+y  calls the int class __add__ method when x is an integer, but it calls the float type's __add__ method when x is a float.

class Dog:
    '''
    This is the constructor for the class. it is called whenever a Dog
    object is created. The reference called "self" is created by python
    and made to point to the space for the newly created object. Python
    does this automatically for us but we have to have "self" as the forst
    parameter to the __init__ method (i.e. the constructor)
    '''
    def __init__(self, name, day, month, year, speakText):
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.speakText = speakText

    '''
    This is the accessor method that returns the speakText stored in the
    object. Notice that "self" is a parameter. Every method has "self" as its
    first parameter. the "self" parameter si a reference to the current
    object. The current object appears on the left hand side of the dot 9i.e.
    the .) when the method is called
    '''
    def speak(self):
        return '{} goes {} {}!!'.format(self.name, self.speakText, self.speakText)

    '''Here is an accessor method to get the name'''
    def getName(self):
        return 'hi my name is {}.'.format(self.name)

    ''' This is another accessor method to get the age'''
    def getAge(self):
        return 'I was born on {}-{}-{}.'.format(self.day,self.month,self.year)

    ''' This is mutator method that changes the speakText of the Dog object'''
    def changeBark(self, bark):
        self.speakText = bark

    '''
    When creating a puppy we don't know it's birthday. Pick the
    first dogs birthday plus one year. the speakText will be the
    concatination  of both dogs text. The dog on the left side of the +
    operator is the object referenced by the 'self' parameter. The
    'otherDog' parameter is the dog on the right side of the + operator.
    '''
    def __add__(self, otherDog):
        return Dog('Puppy of ' + self.name + ' and ' + otherDog.name, \
                   self.month, self.day, self.year + 1, \
                   self.speakText + otherDog.speakText)

def main():
    boyDog = Dog('Mesa', 5, 15, 2004, "WOOOOF")
    girlDog = Dog("Cindy", 5, 6, 2004, "BOWWOWOW")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.getAge())
    print(girlDog.getAge())
    boyDog.changeBark('SNOOP D O DOUBLE G')
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.getName())
    print(puppy.getAge())


if __name__ == '__main__':
    main()













