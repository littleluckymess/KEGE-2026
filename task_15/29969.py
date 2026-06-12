def f(x, y):
    return (x > A) or (y > A) or (x + 2*y < 80)

for A in range(0, 1000)[::-1]:
    if all((f(x, y) for x in range(0, 1000) for y in range(0, 1000))):
        print(A)
        break

