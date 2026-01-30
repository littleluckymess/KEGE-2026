def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        d |= {i, num // i}
    if len(d) > 1:
        return min(d) + max(d)
    return 0

cnt = 0
for N in range(700_001, 10**20):
    M = f(N)
    if M % 10 == 4:
        print(N,M)
        cnt += 1
        if cnt == 5:
            break

