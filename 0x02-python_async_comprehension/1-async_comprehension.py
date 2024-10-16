#!/usr/bin/env python3
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """collect generators results using an async comprehensing."""

    all_vals = []
    async for val in async_generator():
        all_vals.append(val)
    return all_vals
