def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
        if len(d) == 3:
            return max(d)
    return 0

for N in range(int(106_732_567 ** .5), int(152_673_836 ** .5)):
    if M := f(N**2):
        print(N**2, M)



