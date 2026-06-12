def f(x):
    return (x & A == 0) or (not(x & 37 == 0)) or (not( x & 12 == 0))

for A in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break