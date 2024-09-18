"""EX02 - Chardle like Wordle"""

__author__ = "730654179"


# Creating a function definition for input_word
def input_word():
    # Local variable is called word and asks for a five-character word
    word: str = input("Enter a 5-character word: ")
    # Using an if statement for when the length of the local variable is any number but 5
    # Printing an error statement and using exit() to stop the funtion execution
    if len(word) != 5:
        print("Error: Word must contain 5 characters")
        exit()
    return word


# Creating a function definition for input_letter to enter in a single character with a local variable
def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    # Using another if statement for when the character is any length but one
    if len(letter) != 1:
        # Printing an error statement for when the length is not one and stopping the execution with exit()
        print("Error: Character must be a single character.")
        exit()
    return letter


# Creating a function definition for contains_char using the parameters of word and letter
def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    # Local variable called x with an inital value of 0
    index: int = 0
    # Checking if the first character matches the letter
    if str(word)[0] == letter:
        print(letter + " found at index 0")
        # Using a shorthand operator with +=
        index += 1
    # Checking if the second character of the word matches the letter
    if str(word)[1] == letter:
        print(letter + " found at index 1")
        # Using a shorthand operator with +=
        index += 1
    # Checking if the third character of the word matches the letter
    if str(word)[2] == letter:
        print(letter + " found at index 2")
        # Using a shorthand operator with +=
        index += 1
    # Checking if the fourth character of the word matches the letter
    if str(word)[3] == letter:
        print(letter + " found at index 3")
        # Using a shorthand operator with +=
        index += 1
    # Checking if the fifth character of the word matches the letter
    if str(word)[4] == letter:
        print(letter + " found at index 4")
        # Using a shorthand operator with +=
        index += 1
    # Using an if, elif, and else statement for how many instances the
    # Single character or letter is found in the word
    if index == 0:
        print("No instances of " + letter + " found in " + word)
    elif index == 1:
        print(str(index) + " instances of " + letter + " found in " + word)
    else:
        print(str(index) + " instances of " + letter + " found in " + word)


# Defining another function called main as the entry point of the game
# Automatically calls the functions
def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# Allows code to run as a module
if __name__ == "__main__":
    main()
