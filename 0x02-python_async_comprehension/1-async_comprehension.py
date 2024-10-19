#!/usr/bin/env python3
""" This module a coroutine called async_comprehension
that takes no arguments.
The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""
import asyncio
import random
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Async couroutine that iterates through
    another async generator and collects the
    yielded values in a list, this list
    is then returned
    """
    return [value async for value in async_generator()]
