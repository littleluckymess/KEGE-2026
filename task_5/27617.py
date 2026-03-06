ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        R = R + bin(N % 3 * 3)[2:]

    R = int(R, 2)
    ans.append([abs(130 - R),N])

for i in (sorted(ans)[:10]):
    print(*i)
