"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6  # Test case from LeetCode problem
    assert max_subarray_sum([1]) == 1                       # Test for single element
    assert max_subarray_sum([-1]) == -1                    # Test for single negative element
    assert max_subarray_sum([-2,-3,-1]) == -1             # Test for all negative numbers
    assert max_subarray_sum([5,4,-1,7,8]) == 23           # Test for all positive numbers
    assert max_subarray_sum([0,0,0]) == 0                 # Test for all zeros

def test_max_subarray_sum_edge_cases():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1     # Test for all negative numbers with no positive sum
    assert max_subarray_sum([0, -1, 0]) == 0            # Test for zeros with a negative number in between

def test_max_subarray_sum_large_numbers():
    assert max_subarray_sum([100, -1, 100]) == 199  # Test for large numbers

if __name__ == "__main__":
    pytest.main()