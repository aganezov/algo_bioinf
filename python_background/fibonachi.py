# -*- coding: utf-8 -*-
from functools import lru_cache


# when function is annotated with lru_cache every call to the function with distinct arguments is memorized
# no recomputing for the same argument is performed
# works just as efficient as a linear fibonachi algorithm
@lru_cache()
def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)


# linear fibonachi algorithm implementation
def fib1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

print(fib(100))
print(fib1(100))
