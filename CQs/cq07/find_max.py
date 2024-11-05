"""Finding the max value in Challenge Question 7"""

__author__ = "730654179"


# Function definition for find_and_remove_max with one parameter of list[int] and returns int
def find_and_remove_max(list1: list[int]) -> int:
    # If statement for when the list is empty
    if len(list1) == 0:
        # Returning -1 for when the if statement above is true
        return -1

    # Two local variables called i with initial value of 0 and max_ val as list1[int]
    i: int = 0
    max_val: int = list1[i]

    # First while loop to find the max value
    while i < len(list1):
        # If statement with the condition of when the element in list1 is greater than the max_value value
        if list1[i] > max_val:
            max_val = list1[i]
        # Increasing i by an increment of 1
        i += 1

    # Third local variable called idx with an initial value of 0
    idx: int = 0
    # Second while loop to remove all instances of the max value
    while idx < len(list1):
        # If statement for when the element in list1 is equal to the max_value value
        if list1[idx] == max_val:
            # Using pop() to remove an element from a list
            list1.pop(idx)
        else:
            idx += 1

    # Returning the max_val variable
    return max_val
