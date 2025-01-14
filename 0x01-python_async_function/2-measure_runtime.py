#!/usr/bin/env python3
"""Measure time taken to execute a function."""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measurre the time it takes to complet the execution
    of the async function waitn()."""

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time / n
