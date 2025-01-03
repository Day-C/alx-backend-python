#!/usr/bin/env python3
'''annotate correctly.'''
from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')
'''Define response annotation.'''
R = Union[Any, T]
'''Define Default anotation.'''
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    '''return  the value of a key.'''

    if key in dct:
        return dct[key]
    else:
        return default
