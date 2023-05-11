#!/usr/bin/env python3
"""
import wait_random from the previous python file
that you’ve written and write an async routine
called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn
wait_random n times with the specified max_delay
wait_n should return the list of all the delays
(float values). The list of the delays should be
in ascending order without using sort() because
of concurrency
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n"""
    delay_list: List[float] = []
    for i in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
