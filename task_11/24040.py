from math import *
for L in range(10**10):
    N = 1989 + 10 + 52
    i = ceil(log2(N))
    I = ceil(i * L / 8)
    if 836 * I <= 639 * 2**10:
        print(L)


