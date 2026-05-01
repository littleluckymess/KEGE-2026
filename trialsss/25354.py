def f(x, y):
    return (78125 != y + 4*x) or (A > x) and (A > y)
for A in range(1, 78126)[::-1]:
    if all(f(x,y) for x in range(1, 78126) for y in range(1, 78126)):
        print(A)
        break