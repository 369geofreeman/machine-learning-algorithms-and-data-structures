# A basic class structure
# ---


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
Here we can test our class by calling the methods, mutating the boyDog
object, and finally seeing the results of the speakText by calling it again
'''

boyDog = Dog('Mesa', 5, 15, 2006, "WOOOOOF")
girlDog = Dog('Cindy', 5, 6, 2004, "BOW_WOW_WOW")
print(boyDog.speak())
print(girlDog.speak())
print(boyDog.getAge())
print(girlDog.getAge())
boyDog.changeBark('WHIMPER...')
print(boyDog.speak())
