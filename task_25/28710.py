def fact(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i <= num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 1:
        d += [num]

    return d

cnt = 0
for N in range(3_600_001, 10**10):
    M = fact(N)
    if len(M) == 3 and all('3' in str(i) and '5' in str(i) for i in M):
        print(N, max(M))
        cnt += 1
        if cnt == 5:
            break