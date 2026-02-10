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
for N in range(6_086_055 + 1, 10**20):
    d = fact(N)
    if len(d) == 2 and all(str(x).count('6') == 1 for x in set(d)):
        print(N, d[-1])
        cnt += 1
        if cnt == 5:
            break
