#!/usr/bin/env python3
"""generator timer."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """measureasync functions runtime and return results."""

    start_time = time.perf_counter()
    # execute the function 4 times in using asyncio.gather()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - start_time
    return float(elapsed)
