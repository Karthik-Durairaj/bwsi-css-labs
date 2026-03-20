"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]          # Test case from LeetCode problem
    assert two_sum([3, 2, 4], 6) == [1, 2]               # Test for different target
    assert two_sum([3, 3], 6) == [0, 1]                  # Test for duplicate numbers
    assert two_sum([-1, -2, -3, -4], -5) == [1, 2]     # Test for negative numbers
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]          # Test for zeros

def test_two_sum_edge_cases():
    assert two_sum([1, 2, 3, 4], 7) == [2, 3]           # Test for last two numbers
    assert two_sum([1, 2, 3, 4], 3) == [0, 1]           # Test for first two numbers

if __name__ == "__main__":
    pytest.main()