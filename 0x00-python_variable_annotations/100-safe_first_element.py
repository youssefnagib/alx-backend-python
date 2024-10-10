#!/usr/bin/env python3
'''
Module safe_first_element
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Function safe_first_element returns the first element of a sequence,
    or None if the sequence is empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
