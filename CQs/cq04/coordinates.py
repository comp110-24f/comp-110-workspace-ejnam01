"""Coordinates File of Fourth Challenge Question Practicing Importing Functions"""

__author__: str = "730654179"


# Function definition for get_coords that contains 2 str parameters that has a return type of None
def get_coords(xs: str, ys: str) -> None:
    index = 0
    # Using a while loop nested in a while loop
    # Outer while loop checks every character in xs while the inner while loop goes through every character for ys
    while index < len(xs):
        index1 = 0
        while index1 < len(ys):
            print("(" + xs[index] + "," + ys[index1] + ")")
            index1 += 1
        index += 1
