from functools import*
@lru_cache(None)

def f(n):
    if n < 3:
        return 1
    if n % 2 == 0:
        return f(n-1) + n - 1
    return f(n-2) + 2*n-2

print(f(34))