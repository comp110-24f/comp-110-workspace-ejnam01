"""Simple number guessing game for challenge question 2"""

__author__ = "730654179"


def guess_a_number() -> None:
    """establishing the local variable secret number"""
    secret: int = 7
    """another local variable guess for their guess"""
    guess: int = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    """using conditionals to provide feedback about their guess"""
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


# checking the value of a variable by calling a function with an if statement
if __name__ == "__main__":
    guess_a_number()
