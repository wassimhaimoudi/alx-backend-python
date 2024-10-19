#!/usr/bin/env python3
""" This module a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather
"""
import asyncio
from time import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures Runtime for 4 parallel comprehensions
    """
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*task)
    end = time()
    delta = end - start
    return delta
