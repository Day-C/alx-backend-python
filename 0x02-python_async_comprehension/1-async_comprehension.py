#!/usr/bin/env python3i
"""List comprehention."""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect generators results using an async comprehensing."""

    return [val async for val in async_generator()]
