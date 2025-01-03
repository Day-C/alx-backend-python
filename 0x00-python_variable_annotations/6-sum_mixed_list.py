#!/usr/bin/env python3
"""annotated funtion that sums up all arguments of type int & float."""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sum the itemts in the argument list
    Args:
      mxd_list: list of integers and floats
    return: float sum of all items in list
    """

    list_sum = 0
    for i in range(len(mxd_list)):
        list_sum += mxd_list[i]
    return list_sum
