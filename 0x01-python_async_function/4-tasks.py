#!/usr/bin/env python3
'''
Take the code from wait_n
and alter it into a new function task_wait_n.

The code is nearly identical to wait_n
except task_wait_random is being called.
'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async function that spawns wait_random n times with specified max_delay.
    Parameters:
        n (int): Number of times to call wait_random
        max_delay (int): Maximum delay in seconds for each call to wait_random
    Returns:
        list: List of all the delays (float values) in ascending order
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
