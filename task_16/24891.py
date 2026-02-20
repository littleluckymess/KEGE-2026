from functools import lru_cache

@lru_cache(None)
def F(n):
    if n <= 10: return n
    return n - 7 + F(n - 21)

for i in range(0, 186_000):
    F(i)

print((F(185_734) - F(185_650)) / F(40))