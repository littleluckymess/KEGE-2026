from functools import lru_cache
@lru_cache(None)
def f(n):
    if n > 30:
        return f(n-6) + 2048
    return 3*(g(n-5) + 13)

@lru_cache(None)
def g(n):
    if n >= 221_337:
        return 2*n + 50
    return g(n+11) - 48

for i in range(221_340, 0, -1):
    g(i)

for i in range(0, 221_340):
    f(i)

print(f(5078))