def f(x,y):
    return (9*x + y > A) or (x >= 36) or (y >= 18)
for A in range(1, 1000)[::-1]:
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(A)
        break