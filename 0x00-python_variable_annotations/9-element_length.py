#!/usr/bin/env python3
'''
    This module contains a function to get the length of each element in a list.
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Function element_length it returns a list of tuples, where each tuple contains the index and length of an element in the input list.
    '''
    return [(i, len(i)) for i in lst]
