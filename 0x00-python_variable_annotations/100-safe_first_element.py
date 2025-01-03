#!/usr/bin/env python3
'''annotate.'''
from typing import Union, Sequence, Any

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """annotation function to save first element of any type
    Args:
      lst (Any data type)
    Return: item at first index or none.
    """

    if lst:
        return lst[0]
    else:
        return None
