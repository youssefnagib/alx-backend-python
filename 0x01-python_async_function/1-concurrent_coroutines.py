#!/usr/bin/env python3
'''
Import wait_random from the previous python file
that you have written and write an async routine called wait_n
that takes in 2 int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async function that spawns wait_random n times with specified max_delay.
    Parameters:
        n (int): Number of times to call wait_random
        max_delay (int): Maximum delay in seconds for each call to wait_random
    Returns:
        list: List of all the delays (float values) in ascending order
    '''
    task = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for completedTask in asyncio.as_completed(task):
        result = await completedTask
        delays.append(result)
    return delays
