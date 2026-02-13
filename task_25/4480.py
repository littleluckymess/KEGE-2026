from math import prod

def f(num):
    d = set()
    for i in range(1, int(num**.5)+1):
        if num % i == 0:
            d |= {i, num // i}
    if sum(d) % 2 != 0 and prod(d) % 2 != 0:
        if len(d) > 10:
            return len(d)
    return 0

cnt = 0
for N in range(800_001, 10**20):
    if M := f(N):
        print(N, M)
        cnt += 1
        if cnt == 6:
            break

