from math import *

for N in range(1, 10 ** 9):
    L = 2783
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 62_784 * I >= 356 * 2 ** 20:
        print(N)
        break