from math import log2, ceil

L = 377
for N in range(1, 100_000):
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 23155 > 5536 * 2**10:
        print(N)
        break
