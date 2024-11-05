"""Practicing Dictionary Functions for Exercise 06"""

__author__ = "730654179"


# Function definition for invert with one parameter of a dictionary of [str,str] and a return type of a dictionary of [str,str]
def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and the values of the original dictionary"""
    # Local variable to initialize an empty dictionary
    result: dict[str, str] = {}
    # For loop to go through each key value pair in the dictionary
    for key in d:
        # Setting value to be equal to the current key in the dictionary
        value = d[key]

        # If statement for when the value already exists in the result dictionary
        if value in result:
            # Raising a KeyError because dictionary keys must be unique
            raise KeyError("Error! This value already exists.")

        # Inverting the key value pair to the result dictionary
        result[value] = key

    # Returning the result dictionary
    return result


# Function definition for favorite_color with one parameter called input which is a dictionary of [str,str] that has a return type of a string
def favorite_color(input: dict[str, str]) -> str:
    """Finding which color appears the most frequent"""
    # Three local variables
    # output initializing an empty dictionary
    output: dict[str, int] = {}
    # mode will track the most frequent color
    mode = ""
    # max will keep the highest count of a color
    max: int = 0

    # For loop to go through each key value pair in the input parameter
    for inp in input:
        # Defining color to be connected to the current key
        color = input[inp]
        # If statement for when color does not exist in the output dictionary yet
        if color not in output:
            # Setting the count to 0 for that specific color
            output[color] = 0

        # Increase the count of the color by 1
        output[color] += 1

        # If statement to check if the count of the color appears more than the max variable
        if output[color] > max:
            # Assigning the current color to the mode variable because it has the highest count
            mode = color
            # Assigning the output[color] to the max variable to update the count to the count of the color which is the highest
            max = output[color]

    # Returning the mode variable of the most frequent color
    return mode


# Function definition of count with one parameter of a list of strings that returns a dictionary of [str,int]
def count(list1: list[str]) -> dict[str, int]:
    """Counting how many times the value appeared in the input"""
    # Local variable called item_count initializing an empty dictionary
    item_count: dict[str, int] = {}
    # For loop to go through each item in the list
    for item in list1:
        # If statement for when the item already exists in item_count dictionary
        if item in item_count:
            # Increase the count by 1
            item_count[item] += 1
        # If the item does not already exist in the item_count dictionary
        else:
            # Set the count to 1
            item_count[item] = 1
    # Return the dictionary of counts of each item
    return item_count


# Function definition of alphabetizer with a parameter called words which is a list of string that returns a dictionary of [str, list[str]]
def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Organizing the dictionary to the first letter of the word"""
    # Initializing an empty dictionary
    sort: dict[str, list[str]] = {}
    # For loop to go through each element in the list
    for word in words:
        # Using .lower() to take in no argument and return the lower-cased string
        first = word[0].lower()
        # If statement for when the first letter does not exist in the dictionary called sort
        if first not in sort:
            # Add an empty list to the key
            sort[first] = []
        # Append word to the list that is connected to the word
        sort[first].append(word)
    # Returning the dictionary with words organized by the letter
    return sort


# Function definition of update_attendance with three parameters of dict[str,list[str]] and two string parameters with a None return type
def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updating the student's attendance log"""
    # If statement for when the day is already in the attendance_log
    if day in attendance_log:
        # Another if statement for when the day exists but not the specific student
        if student not in attendance_log[day]:
            # Add the student's name to the list of that speciic day with append
            attendance_log[day].append(student)
    # If the day does not exist in the dictionary
    else:
        # Create a new day or key with the name of the day with a new list of students names
        attendance_log[day] = [student]
