#!/usr/bin/env python3
'''Return a function that multiplies a float.'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return another function
    Args: multipier (float)
    Return: a fucntion that multiplies a float by multiplier.
    """

    return lambda x: x * multiplier
