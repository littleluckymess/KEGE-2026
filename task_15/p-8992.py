def DEL(n, m):
    return n % m == 0

def f(x):
    return DEL(x, 21) <= ((not DEL(x, A)) <= (not DEL(x, 77)))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break