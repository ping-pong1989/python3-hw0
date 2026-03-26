"""Lecture 04 practice problems.

Implement each class/function below so tests pass.
Rules:
- Do not change names/signatures.
- Use only the Python standard library.

Problems:
1. log_calls decorator
2. measure_time decorator
3. count_calls decorator
4. ensure_non_negative decorator
5. Retry class decorator
6. Throttle class decorator
7. CallLimit class decorator
8. LruCache class decorator (optional)

"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any
import time
from functools import wraps
from collections import OrderedDict


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())

        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"{func.__name__}({all_args}) -> {result}")
        return result

    return wrapper


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        ms = (end - start) * 1000
        print(f"Executed in {ms:.2f} ms")

        return result

    return wrapper


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def ensure_non_negative(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError("Negative result not allowed")
        return result

    return wrapper


class Retry:
    def __init__(self, times: int) -> None:
        if times < 0:
            raise ValueError("times must be >= 0")
        self.times = times

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempts >= self.times:
                        raise
                    attempts += 1

        return wrapper


class Throttle:
    def __init__(self, interval: float) -> None:
        if interval < 0:
            raise ValueError("interval must be >= 0")
        self.interval = interval

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        last_call = None

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_call
            now = time.perf_counter()

            if last_call is not None and (now - last_call) < self.interval:
                raise RuntimeError("Too many calls")

            result = func(*args, **kwargs)
            last_call = now
            return result

        return wrapper


class CallLimit:
    def __init__(self, limit: int) -> None:
        if limit < 0:
            raise ValueError("limit must be >= 0")
        self.limit = limit

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.calls >= self.limit:
                raise RuntimeError("Call limit exceeded")

            wrapper.calls += 1
            return func(*args, **kwargs)

        wrapper.calls = 0
        return wrapper


class LruCache:
    def __init__(self, maxsize: int) -> None:
        self.maxsize = maxsize

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)
                return cache[args]

            result = func(*args)
            cache[args] = result

            if len(cache) > self.maxsize:
                cache.popitem(last=False)

            return result

        return wrapper