from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 7:
        return 7
    return n + 1 + f(n-2)

for i in range(1, 2025):
    f(i)

print(f(2024) - f(2020))
