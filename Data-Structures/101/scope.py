# Scope
# ---

import math

# ------ The module level ------ #
PI = math.pi

def area(radius):
    # ---- Local scope of area (including radius identifier) ---- #
    theArea = PI * radius ** 2

    return theArea
    # ---- End of area scope ---- #


def main():
    # ---- Local scope of main ----#

    historyOfPrompts = []
    historyOfOutput = []

    def getInput(prompt):
        # --- Local scope of getMain --- 
        x = input(prompt)
        historyOfPrompts.append(prompt)

        return x
        # --- end of getMain scope --- #

    rString = getInput("Please enter the radius of a circle: ")
    r = float(rString)
    val = area(r)

    showOutput("The area of the circle is " + str(val))
    # ---- End of main scope ---- #


if __name__ == "__main__":
    main()

# ------ End of module level scope ------ #



