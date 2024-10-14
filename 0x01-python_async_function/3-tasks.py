#!/usr/bin/env python3
'''
Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
'''
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    A coroutine that waits for a random delay between 0 and max_delay seconds.
    Parameters:
        max_delay (int): Maximum delay in seconds
    Returns:
        asyncio.Task: A task that will wait for the random delay
    '''
    return asyncio.create_task(wait_random(max_delay))
