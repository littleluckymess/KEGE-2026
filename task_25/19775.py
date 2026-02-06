def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            if is_prime(i):
                d |= {i}
            if is_prime(num // i):
                d |= {num // i}
    S = sum(d)
    if S and S % 145 == 0:
        return S
    return 0

cnt = 0
for N in range(32_500_001, 10**20):
    if S:=f(N):
        print(N,S)
        cnt += 1
        if cnt == 7:
            break
