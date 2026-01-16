
def DEL(n,m):
    return n % m == 0
def f(x):
    return (DEL(x,2) <= (x % 3 != 0)) or (x + A >= 80)

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break