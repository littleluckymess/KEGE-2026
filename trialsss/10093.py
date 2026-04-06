from math import log2, ceil
L = 60
N = 10 +250
i = ceil(log2(N))
I = ceil(L * i / 8)
print(I * 65_536 / 2 ** 10)