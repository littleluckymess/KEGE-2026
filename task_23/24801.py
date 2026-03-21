def f1(start, end):
    if start == end: return 1
    if start > end or start == 24: return 0
    return f1(start + 1, end) + f1(start + 2, end) + f1(start + 4, end) + f1(start + 8, end)
res1 = f1(16, 32) * f1(32, 48)

def f2(start, end):
    if start == end: return 1
    if start > end or start == 32: return 0
    return f2(start + 1, end) + f2(start + 2, end) + f2(start + 4, end) + f2(start + 8, end)
res2 = f2(16, 24) * f2(24, 48)
print(res1 + res2)

##############################################################################################

from functools import lru_cache

@lru_cache(None)
def f(start, end, flag24, flag32):
    if start == 24: flag24 = True
    if start == 32: flag32 = True
    if start == end and flag24 + flag32 == 1: return 1
    if start > end or flag24 + flag32 == 2: return 0
    return f(start + 1, end, flag24, flag32) + \
        f(start + 2, end, flag24, flag32) + \
        f(start + 4, end, flag24, flag32) + \
        f(start + 8, end, flag24, flag32)


print(f(16,48, False, False))
