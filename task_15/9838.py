def f(x,y):
    return (x + 2*y > A) or (y < x) or (x < 30)
for A in range(0, 1000):
    if all(f(x,y) for x in range(0,1000) for y in range(0,1000)):
        print(A)
