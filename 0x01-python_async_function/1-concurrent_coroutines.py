#!/usr/bin/env python3
""" This module defines several coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Executes wait_random n times with the specified max_delay and returns
    a list of delays.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay to be passed to wait_random.

    Returns:
        List[float]: A list of delays returned by wait_random.
    """
    list_of_delays: List[float] = [
        await wait_random(max_delay) for _ in range(n)
    ]
    return list_of_delays
