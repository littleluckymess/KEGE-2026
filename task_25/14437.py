def f(num):
    d = set()
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            d |= {i, num // i}
    if len(d) > 0:
        M =sum(d) // len(d)
        if str(M)[-3:] == '313' and M % 1000 == 313:
            return M
    return 0

cnt = 0
for N in range(0, 700_000)[::-1]:
    if M:= f(N):
        print(N,M)
        cnt += 1
        if cnt == 7:
            break
