def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
           if is_prime(i): d |= {i}
           if is_prime(num // i): d |= {num // i}
    if len(d) > 1:
        M = max(d) + min(d)
        if M > 60_000 and str(M) == str(M)[::-1]:
            return M
    return 0

cnt = 0
for N in range(5_400_001, 10**10):
    if M:=f(N):
        print(N, M)
        cnt += 1
        if cnt == 5:
            break



