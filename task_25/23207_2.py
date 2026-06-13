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

    if num > 2:
        d += [num]
    return d

cnt = 0
for N in range(1_324_727 + 1, 10**10):
    M = fact(N)
    if len(M) == 2 and str(M[0]).count('5') == str(M[1]).count('5') == 1:
        if all(str(i).count('5') == 1 for i in M):
            print(N, max(M))
            cnt += 1
            if cnt == 5:
                break


