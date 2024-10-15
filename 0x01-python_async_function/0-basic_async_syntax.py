#!/usr/bin/env python3
""" This module defines a basic coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ waits for n seconds
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
