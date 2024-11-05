"""Fifth Exercise Building List Utility Functions"""

__author__ = "730654179"


# Function definition for only_evens with a parameter of a list of integers to return a list of integers
def only_evens(input: list[int]) -> list[int]:
    """Returning a list of only even number without mutating the list parameter called input"""
    # Two local variables called output which is an empty list of integers and i with an initial value of 0
    output: list[int] = []
    i: int = 0
    # While loop for when i is less than the length of the list
    while i < len(input):
        # If statement for when the element is an even number using % operator because all even numbers are divided by 2
        if input[i] % 2 == 0:
            # Using append() to add the element to the initially empty list of output
            output.append(input[i])
        # Increasing i by a value of 1
        i += 1
    # Returning the list called output
    return output


# Function definition for sub with three parameters: one list of integers and two integer
# Return type of a list of integers
def sub(list1: list[int], start: int, end: int) -> list[int]:
    """Creating a list that is a subset of the list parameter between the other two parameters specifying the start and end"""
    # If statement for when the length of list1 is 0 or when the start integer is greater than the length of the list or when end integer is a negative
    if len(list1) == 0 or start >= len(list1) or end <= 0:
        # Returning an empty list
        return []

    # If statement for when the start integer is negative
    if start < 0:
        # Make the start integer equal a value of 0
        start = 0

    # If statement for when the end integer is greater than the length of the list
    if end > len(list1):
        # Make the end integer equal the integer of length of the list
        end = len(list1)

    # Two local variables called result which is an empty list of integers and i which equals the start parameter
    result: list[int] = []
    i: int = start
    # While loop for when i is less than the end parameter
    while i < end:
        # Adding the element to the initially empty list called result
        result.append(list1[i])
        # Increasing the i variable by one
        i += 1

    # Returning a list called result
    return result


# Function definition called add_at_index with three parameters again: one list of integers and two integers
# Return type is None
def add_at_index(list2: list[int], first: int, second: int) -> None:
    """Mutating the list parameter"""
    # If statement to raise an IndexError with the conditions of second parameter being negative or greater than the length of the list parameter
    if second < 0 or second > len(list2):
        raise IndexError("Index is out of bounds for the input list")

    # Adding 0 to list2 with the append function
    list2.append(0)

    # Local variable called i which is the length of list2 subtracted by 1
    i: int = len(list2) - 1
    # While loop for when i is greater than the parameter called second
    while i > second:
        # Updating the element to the prior element value
        list2[i] = list2[i - 1]
        # Decreasing the i variable by one to go through each element for when i is greater than second
        i -= 1

    # Assigning list2[i] to the value of first
    list2[i] = first
