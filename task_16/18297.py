from functools import*
@lru_cache(None)

def f(n):
    if n < 10:
        return n- 1
    if n >= 10 and n % 2 == 0:
        return 3*n - 1 + f(n-3)
    else:
        return 5*n + 2 + f(n-4)
for i in range(5000): f(i)
print(f(4445) - f(4444))