#!/usr/bin/env python3
'''
write a measure_runtime coroutine
that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime
and return it.

Notice that the total runtime is roughly 10 seconds
, explain it to yourself.
'''
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the total runtime of async_comprehension four times
    in parallel using asyncio.gather.
    Return:
        float: Total runtime in seconds.
    '''
    tasks = [async_comprehension() for _ in range(4)]
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
