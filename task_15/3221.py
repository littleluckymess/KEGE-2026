def f(x):
    return (x % 3 == 0) <= (x % 5 != 0) or (x + A >= 70)
for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break