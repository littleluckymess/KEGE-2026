def f(num):
    d = set()
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            d |= {i,num // i}

    for i in sorted(d):
        if i % 10 == 9 and i != 9:
            return i
    return 0

cnt = 0
for N in range(800_001, 10**20):
    M = f(N)
    if M:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break

