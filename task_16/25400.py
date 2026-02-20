from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 31054:
        return f(n+4) + 3020
    return 3*(g(n-2) - 15)

@lru_cache(None)
def g(n):
    if n >= 28:
        return g(n-5) - 15
    return 3*n - 4

for i in range(0, 31_200):
    g(i)

for i in range(31_100, 0, -1):
    f(i)

print(f(15))