"""Summing the elements of a list using different loops"""

__author__ = "730654179"


# Function definition for w_sum with a parameter of vals which is a list of floats
# Returning the sum of all the elements by going through each element in the list
def w_sum(vals: list[float]) -> float:
    # Setting two local variables called i (acts as the index) and sum1
    i: int = 0
    sum1: float = 0.0
    # Using a while loop to loop through each element in the list
    while i < len(vals):
        # sum1 increases by a value of the element in that list
        sum1 += vals[i]
        # The index increases by one to go through each element
        i += 1
    # Returning the value of sum1
    return sum1


# Function definition for f_sum which is similar to w_sum
def f_sum(vals: list[float]) -> float:
    # Local variable called sum2 with an initial value of 0.0
    sum2: float = 0.0
    # Using a for...in loop to iterate each element
    for val in vals:
        # Increasing sum2 by the value of the element
        sum2 += val
    # Returning sum2 value
    return sum2


# Function definition for f_range_sum() that results the same as prior
def f_range_sum(vals: list[float]) -> float:
    # Local variable called sum3 with an initial value of 0.0
    sum3: float = 0.0
    # Using a for...in range loop to iterate each element within the range
    for idx in range(0, len(vals)):
        # Once again sum3 value increases by the value of the element
        sum3 += vals[idx]
    # Returning sum3 value
    return sum3
