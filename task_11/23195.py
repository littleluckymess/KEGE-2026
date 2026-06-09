from math import ceil, log2

for N in range(1, 10**8):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i  / 8)
    if I * 356_984 >= 54 * 2 ** 20:
        print(N)
        break