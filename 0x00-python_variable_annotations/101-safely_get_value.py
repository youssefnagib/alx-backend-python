#!/usr/bin/env python3
'''
Module safely_get_value
'''
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
Return = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Return:
    '''
    Function safely_get_value returns the value associated with a
    given key in a dictionary,
    or a default value if the key is not present.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
