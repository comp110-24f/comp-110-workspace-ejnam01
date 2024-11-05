"""Third Exercise on Wordle!"""

__author__ = "730654179"


# Defining a function called input_guess with an integer parameter called secret_word_len with a return type of string
def input_guess(secret_word_len: int) -> str:
    """Asking the user to provide a guess that has a correct given length"""
    # Local variable called guess that asks for a certain character word
    guess = input(f"Enter a {secret_word_len} character word: ")
    # Using a while loop where the length of the local variable guess does not equal the number entered in
    while len(guess) != secret_word_len:
        # Printing out a statement with an f-string
        print(f"That wasn't {secret_word_len} chars! Try again: ")
        # Asking for another input to try again
        guess = input()
    # Returning the local variable
    return guess


# Function definition for contains_char with two string parameters (secret_word and char_guess) that returns a bool value
def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checking if an index of a string parameter matches the second string parameter"""
    # Using an assert statement to test if char_guess is equal to 1
    assert len(char_guess) == 1
    # Creating two local variables called idx with an initial value of 0 and in_the_word
    idx: int = 0
    in_the_word: bool = False
    # While loop for when  idx is less than the length of the word and if the secret_word's character of the index matches the char_guess then the bool turns true
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            in_the_word = True
        # If not, the index increases by one
        idx += 1
    return in_the_word


# Function definition for emojified with two string parameters called guess and secret that returns a string value
def emojified(guess: str, secret: str) -> str:
    """Comparing two strings that have the same length"""
    # Using an assert statement to make sure that the length of the guess will equal the length of the secret
    assert len(guess) == len(secret)
    # Creating emojis using string
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # Two local variables called i for the index and the result
    i: int = 0
    result: str = ""
    # Using a while loop for when the local variable i is less than the length of the guess
    while i < len(guess):
        # if statement for when the two characters match both position and character
        if guess[i] == secret[i]:
            # Provide a green box emoji
            result += GREEN_BOX
        # elif for when a character exists within the secret but does not match the position
        elif contains_char(secret, guess[i]):
            # Provide a yellow box emoji
            result += YELLOW_BOX
        # else statement that is for any condition that does not match the above
        else:
            # Provide a white box emoji
            result += WHITE_BOX
        # Increase the i by 1 to go through each character as long as the variable is less than the length of the guess
        i += 1
    return result


# Function definition for main with one string parameter called secret that returns None
def main(secret: str) -> None:
    """Point of entry of the program and main game loop."""
    # Starting with the first turn and creating a local variable called turn with an initial value of 1
    turn = 1
    # Using a while loop for when the number of turns they have had is less than or equal to the max number of turns (6)
    while turn <= 6:
        # Printing the turn number with an f-string
        print(f"=== Turn {turn}/6 ===")
        # Making sure that the length of the secret matches the input of the guess
        guess = input_guess(len(secret))
        # Printing the results
        print(emojified(guess, secret))
        # Using an if else statement for when the guess matches the secret
        if guess == secret:
            # In the case that they are equal, a winning f-string statement is printed
            print(f"You won in {turn}/6 turns!")
            return
        # Increasing the turn variable by one until it reaches the max number of turns
        turn += 1
    # Printing out a statement to try again tomorrow once the while loop turns false
    print("X/6 - Sorry, try again tomorrow!")


# Allows the code to run as a module
if __name__ == "__main__":
    main(secret="codes")
