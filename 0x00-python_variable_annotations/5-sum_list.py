#!/usr/bin/env python3
'''annotated function that returns sum of float list.'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sums the items of the list argument
    Args:
      input_list: (list of float point numbres)
    return: float ( sun of input_list).
    """

    list_sum = 0
    for i in range(len(input_list)):
        list_sum += input_list[i]
    return list_sum
