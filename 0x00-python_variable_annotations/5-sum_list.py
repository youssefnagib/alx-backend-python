#!/usr/bin/env python3
'''
    This module contains a function to return the sum of all numbers in a list.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of all numbers in a list.

    Args:
        input_list (list): A list of numbers.

    Returns:
        float: The sum of all numbers in the list.
    """
    return sum(input_list)
