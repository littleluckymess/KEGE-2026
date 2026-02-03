def f(num):
    d = set()
    for i in range(2, int(num**.5)+ 1):
        if num % i == 0:
            if i % 2 != 0: d |= {i}
            if num // i % 2 != 0: d |= {num // i}

    if len(d) == 3:
        return sorted(d)
    return []

for N in range(18_782, 18_823):
    if M := f(N):
        print(*M)
