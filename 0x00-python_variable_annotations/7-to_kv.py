#!/usr/bin/env python3
'''
    This module contains a function to convert a key-value pair into a tuple.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to convert a key-value pair into a tuple.

    Args:
        k (str): The key.
        v (int or float): The value.

    Returns:
        Tuple[str, float]: A tuple containing the key and value.
    """
    return (k, v ** 2)
