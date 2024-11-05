"""Fifth Exercise Testing Utility Functions"""

__author__ = "730654179"

# Importing functions from a different file
from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index

# Importing pytest to catch the exception of IndexError
import pytest


# Edge case for only_evens for when the list contains no even numbers
def test_only_evens_empty() -> None:
    """Testing only_evens for when the list has no even number"""
    assert only_evens([1, 3, 5, 9]) == []


# Use case for what the function should return
def test_only_evens_mixed() -> None:
    """Testing only_evens with a list of mixed numbers"""
    assert only_evens([10, 13, 14, 15]) == [10, 14]


# Use case for if the function mutates and should not be mutating
def test_only_evens_mutation() -> None:
    """Tests only_evens if mutating the list"""
    a: list[int] = [4, 6, 7, 11]
    only_evens(a)
    assert a == [4, 6, 7, 11]


# Edge case for sub
def test_sub_out_range() -> None:
    """Tests sub with a negative start and greater end to get the whole list"""
    assert sub([1, 2, 3], -1, 5) == [1, 2, 3]


# Use case for what is expected to be returned with normal integers as the parameters
def test_sub_normal() -> None:
    """Tests sub with normal start and end to get a shorter list"""
    assert sub([5, 6, 7, 8], 1, 3) == [6, 7]


# Use case for if the function undergoes mutation and it should not
def test_sub_mutation() -> None:
    """Tests sub if mutation occurs and to expect the the same list"""
    a: list[int] = [1, 4, 6, 7]
    sub(a, 1, 3)
    assert a == [1, 4, 6, 7]


# Edge case for add_at_index to raise at IndexError using pytest.raises to catch the exception
def test_add_at_index_raise() -> None:
    """Test add_at_index to raise an IndexError"""
    a: list[int] = [33, 22, 1]
    with pytest.raises(IndexError):
        add_at_index(a, 3, 4)


# Use case for add_at_index to test and expect an expected return value
def test_add_at_index_valid() -> None:
    """Tests add_at_index to insert an element at a valid spot"""
    b: list[int] = [5, 10, 20, 30]
    add_at_index(b, 25, 3)
    assert b == [5, 10, 20, 25, 30]


# Use case for when the function should mutate its input
def test_add_at_index_start() -> None:
    """Tests add_at_index to insert an element at the start of the list"""
    c: list[int] = [3, 6, 9, 12, 15]
    add_at_index(c, 10, 0)
    assert c == [10, 3, 6, 9, 12, 15]
