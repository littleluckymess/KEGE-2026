from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    return 2*n - 8 + f(n - 2) + f(n - 1) // 8
print(f(163))