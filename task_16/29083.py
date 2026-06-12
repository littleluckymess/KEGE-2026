from sys import setrecursionlimit

def F(n):
    if n < 17: return 6
    return (n + 5) * F(n - 9)

setrecursionlimit(234_561 // 9 + 100)
print((F(234_561) // 436 + F(234_552) // 218) // F(234_534))


###################################

from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 17: return 6
    return (n + 5) * F(n - 9)

for i in range(0, 234_561):
    F(i)

print((F(234_561) // 436 + F(234_552) // 218) // F(234_534))

###################################

F = [0] * 234_562

for n in range(0, 234_561 + 1):
    if n < 17: F[n] = 6
    else: F[n] = (n + 5) * F[n - 9]

print((F[234_561] // 436 + F[234_552] // 218) // F[234_534])
