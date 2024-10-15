# 0x02. Python - Async Comprehension

## Description

This project covers **asynchronous programming** in Python, specifically focusing on **async comprehensions**. You'll learn how to handle asynchronous iterators and generators, and how to use them efficiently in your programs.

Async programming is important when dealing with operations that might take time (like fetching data from a web API or reading files), allowing Python to perform other tasks in the meantime. With async comprehensions, you can elegantly work with asynchronous sequences while maintaining readable and efficient code.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and use asynchronous generators.
- Write async comprehensions.
- Handle asynchronous iteration over sequences.
- Combine async comprehensions with `async for` loops.
  
## Requirements

- **Python 3.7+** is required to run these scripts.
- Familiarity with **asyncio** library in Python.
- Prior understanding of Python comprehensions is recommended.

## Files

### 1. `0-async_generator.py`
- **Objective:** Write a coroutine called `async_generator` that generates random numbers asynchronously.
- **Description:** The coroutine will loop 10 times, each time asynchronously yielding a random float number between 0 and 10, with a 1-second delay between each yield.

### 2. `1-async_comprehension.py`
- **Objective:** Write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over the `async_generator`, then returns the collected numbers.
- **Description:** The function demonstrates how async comprehensions can be used to gather data from asynchronous sources.

### 3. `2-measure_runtime.py`
- **Objective:** Write a coroutine called `measure_runtime` that measures the total runtime of running `async_comprehension` four times in parallel using `asyncio.gather()`.
- **Description:** This task demonstrates the efficiency of parallel execution in async functions and how to measure execution time.

## Usage

Clone the repository and run the files using Python 3.7+.

```bash
$ git clone https://github.com/your-username/0x02-python-async-comprehension.git
$ cd 0x02-python-async-comprehension
