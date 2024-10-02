"""Lesson for Sept 25"""


def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if not (msg[index] == char):
            copy += msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))
