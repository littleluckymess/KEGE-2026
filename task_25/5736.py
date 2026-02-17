def f(num):
    d = set()
    for i in  range(2, int(num**.5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    if d and max(d) % 7 == 0:
        return max(d)
    return 0

cnt = 0
for N in range(10 ** 9 + 1, 10 ** 20):
        if str(N) == str(N)[::-1] and (M:= f(N)):
                print(N, M)
                cnt += 1
                if cnt == 5:
                    break




