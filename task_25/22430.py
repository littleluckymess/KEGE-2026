def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    d = set()
    a = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(x // i): d |= {x // i}
    a = sorted(a)
    return a[0] + a[1] + a[-1] + a[-2] if len(a) > 3 else 0


cnt = 0
for i in range(456790, 10 ** 15):
    if m := f(i):
        if m % 114 == 39:
            cnt += 1
            print(i, m)
            if cnt == 5:
                break
