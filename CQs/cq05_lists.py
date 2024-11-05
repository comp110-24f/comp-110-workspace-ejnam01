"""Mutating functions."""

__author__ = "730654179"


# Function definition for manual_append with two parameters that returns nothing
# Parameter a being a list[int] and parameter i being an int
def manual_append(a: list[int], i: int) -> None:
    # Mutating the input by appending the i parameter
    a.append(i)


# Function definition for double with only one parameter called a that is a list[int]
# Returns nothing as well
def double(a: list[int]) -> None:
    # Creating a local variable called idx with an initial value of 0
    idx: int = 0
    # Using a while loop for when the local variable is less than the length of the list
    while idx < len(a):
        # Creating an index which doubles the current element in the list
        a[idx] *= 2
        # Increasing the value of idx by one to go through each element in the list
        idx += 1


# Global variable called list_1 with a value of [1,2,3] and is a list[int]
list_1: list[int] = [1, 2, 3]
# Another global variable called list_2 for which the list[int] is the same as list_1
list_2: list[int] = list_1

# Calling the double function with an argument list_2
double(list_2)
# Printing both list_1 and list_2
print(list_1)
print(list_2)
