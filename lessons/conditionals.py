"""Practicing My Conditionals"""


def less_than_10(num: int) -> None:
    """tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # check if this is true
        print("small number!")
        # return True  # "then" block
    else:
        print("big number!")
        # return False
    print("have a nice day!")


less_than_10(num=7)


"""def wake_up(alarm: bool) -> str:
    #Return a message based on if alarm is going off
    if alarm is True:
        return "Wake up! Go to COMP 110"
    else:
        return "Keep sleeping. you deserve it!"


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="s"))"""
