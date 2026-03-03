def f(x,y):
    return (x - 3*y < A) or (y > 400) or (x > 56)
for A in range(1, 1000):
    if all(f(x, y) for x in range(1,1000) for y in range(1, 1000)):
        print(A)
        break