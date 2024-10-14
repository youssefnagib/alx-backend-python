#!/usr/bin/env python3
'''
Create a measure_time function with integers n
and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay)
and returns total_time / n. Your function should return a float.

Use the time module to measure an approximate elapsed time.
'''

import time
import asyncio
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure the total execution time for wait_n(n, max_delay)
    and returns total_time / n.
    Parameters:
        n (int): Number of times to call wait_n
        max_delay (int): Maximum delay in seconds for each call to wait_n
    Returns:
        float: Total execution time divided by n, or None if n is 0
    '''
    # if n == 0:
    #     return None

    start_time = time.time()
    for _ in range(n):
        asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
