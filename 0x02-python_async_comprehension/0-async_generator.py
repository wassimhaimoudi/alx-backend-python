#!/usr/bin/env python3
""" This module defines an asynchronous generator called
async_generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async generator that yields a random float
    number between 0 and 10, with a 1 sec delay
    between each number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
