#!/usr/bin/python3
"""Simple async generator."""
import asyncio
import random


async def async_generator() -> int:
    """loops specific number of times and yields a random number each time."""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
