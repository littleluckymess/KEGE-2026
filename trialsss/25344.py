from string import printable as alph

def convert(num, sys):
    res = ''
    while num != 0:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

for N in range(1, 100_000):
    R = convert(N, 3)
    S = convert(sum(map(int, R)), 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + S
    R = int(R, 3)
    if R % 2 == 1 and R > 208:
        print(R)
        break

