"""Concatenation File of Fourth Challenge Question Practicing Importing Functions"""

__author__: str = "730654179"


# Defining a function called concat with two string parameters and will return a str
def concat(a: str, b: str) -> str:
    # Concatenate the two inputs by using the +
    return a + b


# Suppressing the function call by adding the if __name__ == "__main__" which will allow the function to run and be called within the file but not when imported
if __name__ == "__main__":
    # Global variables called word1 and word2
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
