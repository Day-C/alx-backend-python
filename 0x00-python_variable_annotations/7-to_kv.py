#!/usr/bin/env python3
'''take a string and return a tuple.'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """return a tuple of args
    Args:
      k: string
      v: either integer or float
    return: a tuple.
    """

    tupl = (k, v * v)
    return tuple(tupl)
