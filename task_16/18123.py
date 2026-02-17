from functools import*
@lru_cache(None)

def f(n):
    if n >= 2010:
        return n
    else:
        return f(n+3) + f(n+2) + f(n+1)

for i in range(3000): f(i)
print((f(2000) - 2*(f(2002) +f(2003))) / f(2004))