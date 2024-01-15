import functools
import sys

sys.setrecursionlimit(10**6)

@functools.cache
def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)

n = int(input())
print(f(n))