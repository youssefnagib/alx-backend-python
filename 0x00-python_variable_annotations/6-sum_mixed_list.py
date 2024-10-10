#!/usr/bin/env python3
'''
    This module contains a function to return the sum of all numbers in a list.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    function sum_mixed_list it sum all in list
    Args:
        mxd_lst (list): A list of integers and/or floats.
    Returns:
        float: The sum of all numbers in the list.
    '''
    return sum(mxd_lst)

