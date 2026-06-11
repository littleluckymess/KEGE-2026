def f(x, y):
    return (2*x + y != 110) or (x < y) or (A < x)

for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)