def DEL(n, m):
    return n % m == 0

def f(x):
    P = 2508 <= x <= 2570
    return DEL(x, A) or (P <= (not DEL(x, 214) or (x + A <= 5286)))

for A in range(1, 3000)[::-1]:
    if all(f(x) for x in range(1, 3000)):
        print(A)
        break