def f(x):
    return ((x & 52 != 0) and (x & 48 == 0)) <= (not(x & A == 0))

for A in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break