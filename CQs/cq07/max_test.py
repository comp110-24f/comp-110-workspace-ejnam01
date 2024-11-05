"""Testing the max value in Challenge Question 7"""

__author__ = "730654179"

from CQs.cq07.find_max import find_and_remove_max


# Function names must be different for each test to work
def test_find_and_remove_max() -> None:
    """Testing if the function returns the expected value"""
    b: list[int] = [6, 1, 3, 7, 9]
    assert find_and_remove_max(b) == 9


def test_mutate_find_and_remove_max() -> None:
    """Testing if the function mutates correctly"""
    c: list[int] = [22, 54, 67, 28, 23]
    find_and_remove_max(c)
    assert c == [12, 13, 14]


# The assert is used in a way that allows the mutation to occur


def test_edge_find_and_remove_max() -> None:
    """Testing if the function returns the right value when the input is unconventional"""
    d: list[int] = []
    assert find_and_remove_max(d) == -1


# Unconventional input is when the list is empty
