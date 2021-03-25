# Reading multi-line records from a file
# ---

# To read a multi-line file we need a 'loop and a half' usina while loop rather than a for loop. 
# We write our loop and a half to read the forst line of each recod and then check that line (i.e graphics command) so we know how many more lines to read.

import turtle


def main():
    filename = input("please enter the drawing filename: ")

    t = turtle.Turtle()
    screen = t.getscreen()

    file = open(filename, 'r')

    # Here we have the half a loop to get things started. Reading our first
    # grapghics command here lets us determin if the file is empty or not.
    command = file.readline().strip()

    # if the command is empty, then there are no more commands left in
    # the file
    while command != '':

        # Now we must read the rest of the record and then process it. Because
        # records are variable length, we'll use an if-elif to determin which type of record it is and then we'll read and process the record.

        if command == 'goto':
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == 'circle':
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == 'beginfill':
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file: ", command)

    # Close the file
    file.close()

    t.ht()
    screen.exitonclick()
    print("Program Execution Completed")


if __name__ == "__main__":
    main()




