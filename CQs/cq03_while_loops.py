"""Using the While loop for a challenge question"""

__author__ = "730654179"


# Writing the function definition for num_instances with two string parameters that
# will return an integer
def num_instances(phrase: str, search_char: str) -> int:
    # Creating two local variables called count and index with an initial value of 0
    count: int = 0
    index: int = 0
    # Using a while loop for the phrase and counting the number of search_chars
    # are within the phrase
    while index < len(phrase):
        # Checking the character of the phrase with the search_char value
        if phrase[index] == search_char:
            count += 1
        # Moving on to the next character of the phrase
        index += 1

    # Returning the final value
    return count
