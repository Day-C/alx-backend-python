#!/usr/bin/env python3
"""import another async function."""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """Call the wait_random function n number of times and
    return it's results in an array."""

    results: list = []
    j: int = 0
    while j < n:
        val = await wait_random(max_delay)
        results.append(val)
        j += 1

    j: int = 0
    while j < len(results) - 1:
        i: int = 0
        for i in range(len(results) - 1):
            if results[i] > results[i + 1]:
                temp = results[i + 1]
                results[i + 1] = results[i]
                results[i] = temp
        j += 1
    return (results)
