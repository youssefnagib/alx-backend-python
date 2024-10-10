#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function returns a new function that multiplies its input by a given multiplier.

    Parameters:
    multiplier (float): The value by which the input will be multiplied.

    Returns:
    Callable[[float], float]: A function that takes a float as input and returns the input multiplied by the given multiplier.
    """
    def multiply(n: float) -> float:
        """
        The inner function that performs the multiplication.

        Parameters:
        n (float): The input number.

        Returns:
        float: The input multiplied by the given multiplier.
        1.0: The default multiplier value.
        """
        return n * multiplier
    return multiply
