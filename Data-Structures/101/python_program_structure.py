# The Python Program Structur

'''
One function definition is written in Python called the Main function
This function containes code the program typically sxecutes when it is
first started.
'''

# Imports at the top
import turtle


# other functions definitions followed by the main function definition
def main():
    # The main code of the program goes here
    t = turtle.Turtle()

# This code calls the main function to get everything started. the condition in this
# if statement evaluates to True when the  module is executed by the interpreter, but
# not when it is imported in another module
if __name__ == '__main__':
    main()

# The if statement at the end of the code is the first code executed after teh import statements.

