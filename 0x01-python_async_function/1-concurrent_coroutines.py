#!/usr/bin/env python3
"""import another async function."""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def sorter(array: list) -> list:
    """sort an array in ascending order."""

    j = 0
    while j < len(array) - 1:
        i = 0
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
        j += 1
    return array


async def wait_n(n: int, max_delay: int) -> list:
    """Call the wait_random function n number of times and
    return it's results in an array."""

    results = []
    j = 0
    while j < n:
        val = await wait_random(max_delay)
        results.append(val)
        j += 1

    return sorter(results)
