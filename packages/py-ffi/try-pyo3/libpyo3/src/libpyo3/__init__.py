from .libpyo3 import *

__doc__ = libpyo3.__doc__
if hasattr(libpyo3, "__all__"):
    __all__ = libpyo3.__all__


def fib_slow(n: int) -> float:
    return fib(n)


def fib_fast(n: int) -> float:
    return fib2(n)
