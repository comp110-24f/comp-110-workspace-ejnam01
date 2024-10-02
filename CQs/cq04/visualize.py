"""Visualize File of Fourth Challenge Question Practicing Importing Functions"""

__author__: str = "730654179"

# Importing concat function from concatenation.py
from CQs.cq04.concatenation import concat

# Calling the concat function with global variables
x = "123"
y = "abc"
print(concat(x, y))

# Importing get_coords function from coordinates.py
from CQs.cq04.coordinates import get_coords

# Calling get_coords with the global variables from above
get_coords(x, y)
