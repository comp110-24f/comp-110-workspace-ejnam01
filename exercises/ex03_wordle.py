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
    # Using a for statement to go through each character in secret_word
    for char in secret_word:
        if char == char_guess:
            # Returning a True value if the char_guess is found in the secret_word
            return True
    # Returning false if not
    return False


# Creating emojis using string
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# Function definition for emojified with two string parameters called guess and secret that returns a string value
def emojified(guess: str, secret: str) -> str:
    """Comparing two strings that have the same length"""
    # Using an assert statement to make sure that the length of the guess will equal the length of the secret
    assert len(guess) == len(secret)
    # An empty string that will hold all of the feedback of emojis
    emoji_result = ""

    # Using another for statement to go through each element or character in the guess
    for i in range(len(guess)):
        # If, elif, and else statements
        # If statement for when the first element of the guess and secret are the same
        if guess[i] == secret[i]:
            # Adding a green box emoji when the character is in the right place and the right character
            emoji_result += GREEN_BOX
        # elif statement for when the character is correct but not the position
        elif contains_char(secret, guess[i]):
            # Adding a yellow box emoji
            emoji_result += YELLOW_BOX
        # else statement for any result that does not match the two conditions above
        else:
            # Provide a white box emoji
            emoji_result += WHITE_BOX
    # Returning the emoji_result with emojis
    return emoji_result


# Function definition for main with one string parameter called secret that returns None
def main(secret: str) -> None:
    """Point of entry of the program and main game loop."""
    # Maximum number of turns allowed
    max_turns = 6
    # Starting with the first turn
    turn_number = 1
    # To know when the player has won
    has_won = False
    # Using a while loop for when the number of turns they have had is less than or equal to the max number of turns (6) and the player has not won
    while turn_number <= max_turns and not has_won:
        # Printing the turn number with an f-string
        print(f"=== Turn {turn_number}/{max_turns} ===")
        # Making sure that the length of the secret matches the input of the guess
        guess = input_guess(len(secret))
        # Gaining emojis as the result
        result = emojified(guess, secret)
        # Printing the result
        print(result)

        # Using an if else statement for when the guess matches the secret
        if guess == secret:
            # In the case that they are equal, a winning f-string statement is printed
            print(f"You won in {turn_number}/{max_turns} turns!")
            # Shows that they won
            has_won = True
        # else statement for anything else that occurs other than the condition above
        else:
            # Increasing the turn_number by 1 when they haven't matched the two
            turn_number += 1
    # If statement for when the player has not won after the 6 maximum turns
    if not has_won:
        # Printing out an f-string statement to try again tomorrow
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


# Allows the code to run as a module
if __name__ == "__main__":
    main(secret="codes")
