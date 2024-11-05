"""Fourth exercise using idiomatic Python"""

__author__ = "730654179"


# Function definition of all with two parameters (one being a list of ints and an int) that returns a bool
def all(list1: list[int], num: int) -> bool:
    """Iterating through each element in the list to see if it is equal to num"""
    # Local variable i to act as the index by giving it an initial value of 0
    i: int = 0
    # While loop for when the local variable is less than than the length of the list
    while i < len(list1):
        # When true, this code block runs to check if the element in the list is not equal to the second parameter
        if list1[i] != num:
            # If the if statement is true then a False is returned
            return False
        # The local variable increases by one to check the next element
        i += 1
    # Returning False for when the list is empty using an if statement
    if len(list1) == 0:
        return False
    return True


# Function definition for max that has one parameter, a list of ints, that returns an int
def max(list2: list[int]) -> int:
    """Returning the maximum value of an integer in the list"""
    # If statement for when the list is empty and resulting in ValueError
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    # Local variable called i to act as the index that has an initial value of 0
    i: int = 0
    # Local variable called largest to compare the rest of the values in the list
    largest: int = list2[i]
    # While loop for when i is less than the length of the list
    while i < len(list2):
        # When i is less than the length of the list, then the code encounters an if statement
        # If statement for when the element of list is greater than the first element of the list
        if list2[i] > largest:
            largest = list2[i]
        # Increasing i by one to iterate each element
        i += 1
    # Returning the local variable that will be the largest value in the list due to largest = list2[i]
    return largest


# Function definition for is_equal that has two parameters of which are lists of ints and returns bool
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Ensuring that both lists equal one another"""
    # Two local variables called i and count both having initial value of 0
    i: int = 0
    count: int = 0
    # Using a while loop for when i is less than the length of both list parameters
    while i < len(list_1) and i < len(list_2):
        # If statement for when the two elements or values equal one another
        if list_1[i] == list_2[i]:
            # Increase the count variable by 1
            count += 1
        # Increase the i variable by 1
        i += 1
    # If else statement for when the count equals the length of both list parameters
    if count == len(list_1) and count == len(list_2):
        # Returning true if the condition is met
        return True
    else:
        # Returning false for any other condition than the above condition
        return False


# Function definition of extend with two parameters that are lists of ints and the function returns nothing
def extend(lista: list[int], listb: list[int]) -> None:
    """Extending or adding one list to another list"""
    # Local variable i with an initial value of 0 to act as the index
    i: int = 0
    # While loop for when i is less than the length of the second list parameter
    while i < len(listb):
        # Mutating the first list by appending the second list using append
        # Appending the values of the second list to the end of the first list
        lista.append(listb[i])
        # Increasing i by one to iterate through each element of the list
        i += 1
