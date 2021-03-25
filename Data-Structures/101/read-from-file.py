# Read from a file
# ---

# Here we will read from the file 'draw_instructions.txt' which are a set of instruction that turtle will do the appropriate graphics commands for each record in teh file.
# A for loop will read each command from each line of the file.


# Imports the turtle graphics module
import turtle


# The main function is where the main code of the program si written.
def main():
    # This line reads a line of input from the user
    filename = input('Please enter drawing filename: ')

    # Create a Turtle Graphics window to draw in.
    t = turtle.Turtle()
    # The screen is used at the end of the program
    screen = t.getscreen()

    # The next line opens the file for 'r' or reading. 'w' would open it for
    # Writing, and 'a' would open teh file ot append to it (i.e. add to the
    # end). In this program we are only interested in reading the file.
    file = open(filename, 'r')

    # The following for loop reads the lines of the file, one at a time
    # and executes the body of the loop once for each line of the file.
    for line in file:

        # The strip method strips off the newline character at the end of teh line
        # and any blanks that might be at the beginning or end of the line.
        text = line.strip()

        # The following line splits the text variable into its pieces.
        # For instance, if text contained "goto, 10, 20, 1, black" then
        # commandList will be equal to ["goto", '10', '20'], '1', 'black'] after
        # splittin text.
        commandList = text.split(',')

        # Get the drawing command
        command = commandList[0]

        if command == 'goto':
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[1])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == 'circle':
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == 'beginfill':
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == 'endfill':
            t.end_fill()
        elif command == 'penup':
            t.penup()
        elif command == 'pendown':
            t.pendown()
        else:
            print('Unknown command found in file: ', command)

    # Close the file
    file.close()

    # hide the turtle that we used to draw the picture.
    t.ht()

    # This causes the program to hold the turtle graphics window open
    # untill the mouse id clicked.
    screen.exitonclick()
    print('Program Execution Completed.')


# This code calls the main function to get everything started
if __name__ == '__main__':
    main()

