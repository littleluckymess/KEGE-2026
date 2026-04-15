def f(num):
    d = set()
    for i in range(2, int(num** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    for i in sorted(d):
       if i != 11 and i % 100 == 11:
           return i
    return 0

cnt = 0
for N in range(1_350_051, 10**10):
    if M := f(N):
        print(N,M)
        cnt += 1
        if cnt == 5:
            break