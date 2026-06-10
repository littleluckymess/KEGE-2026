def f(x, y):
    return (x < A) and (y < 3*A) or (2*x + y > 128)
for A in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break