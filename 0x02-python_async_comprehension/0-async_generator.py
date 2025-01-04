#!/usr/bin/env python3
"""Simple async generator."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops specific number of times and yields a random number each time."""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
