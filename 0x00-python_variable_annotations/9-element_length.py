#!/usr/bin/env python3
'''annotate function correctly.'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''get a list of tuple integers.'''

    return [(i, len(i)) for i in lst]
